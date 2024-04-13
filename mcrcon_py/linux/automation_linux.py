import logging
import multiprocessing
import re
import time
from mcrcon import MCRcon
import toml
# 配置日志记录
logging.basicConfig(filename=r'\minecraft-mcrcon\log\server.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# 从配置文件加载设置
def load_settings(filename):
    with open(filename, 'r') as file:
        settings = toml.load(file)
    return settings
# 连接到Minecraft服务器
def connect_to_server(settings):
    host = settings['server']['host']
    port = settings['server']['port']
    password = settings['server']['password']
    return MCRcon(host, password, port)
# 打开数据可视化程序
# 发送欢迎消息给新玩家
def send_message(rcon, name, messages):
    for message in messages:
        try:
            rcon.connect()
            rcon.command(f'tell {name} {message}')
        except Exception as e:
            logging.error(f"Failed to send message to {name}: {e}")
        finally:
            rcon.disconnect()
            time.sleep(2)  # 每条消息间隔2秒

# 从文件加载已加入的玩家列表
def load_joined_players(filename):
    try:
        with open(filename, 'r') as file:
            joined_players = file.read().splitlines()
        return joined_players
    except FileNotFoundError:
        return []

# 将已加入的玩家列表保存到文件中
def save_joined_players(filename, joined_players):
    with open(filename, 'w') as file:
        for player in joined_players:
            file.write(player + '\n')

# 定时清理地面物品
def clear_items(rcon, clear_interval):
    while True:
        try:
            rcon.connect()
            rcon.command('kill @e[type=item]')
        except Exception as e:
            logging.error(f"An error occurred while clearing items: {e}")
        finally:
            rcon.disconnect()
            time.sleep(clear_interval)  # 每30分钟清理一次

# 监控玩家加入和退出服务器
def monitor_players(rcon, messages, joined_players_filename):
    prev_player_count = 0
    joined_players = load_joined_players(joined_players_filename)
    while True:
        try:
            rcon.connect()
            status = rcon.command('list')
            match_names = re.findall(r'§6default§r: (.*)', status)
            if match_names:
                name_list = [re.sub(r'§.', '', name) for name in match_names[0].split(',')]
                for player in name_list:
                    if player not in joined_players:
                        joined_players.append(player)
                        print(f'Player {player} joined the server')
                        send_message(rcon, player, messages)  # 发送欢迎消息
            else:
                joined_players.clear()

            match_numbers = re.findall(r'\d+', status)
            current_player_count = int(match_numbers[1]) if match_numbers else 0
            for player in joined_players:
                if player not in name_list:
                    joined_players.remove(player)
                    print(f'Player {player} left the server')

            if current_player_count != prev_player_count:
                print(f'Current players online: {current_player_count}')
                if current_player_count != 0:
                    print(f'Joined players: {joined_players}')
                prev_player_count = current_player_count
            save_joined_players(joined_players_filename, joined_players)

        except Exception as e:
            logging.error(f"An error occurred while monitoring players: {e}")
        finally:
            rcon.disconnect()
            time.sleep(5)  # 每3秒检查一次

def main():
    settings = load_settings(r'\minecraft-mcrcon\config\config.toml')
    rcon = connect_to_server(settings)
    messages = [
        '欢迎来到服务器！',
        '请遵守服务器规则，享受游戏！',
        '如果您有任何问题，请联系管理员。'
    ]
    clear_interval = 1800  # 30分钟清理一次
    joined_players_filename = r'\minecraft-mcrcon\joined_players.txt'  # 存储已加入玩家列表的文件路径
    clear_process = multiprocessing.Process(target=clear_items, args=(rcon, clear_interval))
    monitor_process = multiprocessing.Process(target=monitor_players, args=(rcon, messages, joined_players_filename))

    clear_process.start()
    monitor_process.start()
    clear_process.join()  # 等待清理任务完成
    monitor_process.join()  # 等待监控任务完成
if __name__ == '__main__':
    main()

