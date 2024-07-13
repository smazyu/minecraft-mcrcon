import toml
import logging
import re
import os
from mcrcon import MCRcon


logging.basicConfig(filename=r'log\server.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def load_settings(filename):
    """Load server settings from a TOML file."""
    if not os.path.exists(filename):
        print(f"未找到配置文件 {filename}，正在生成...")
        print(f"Configuration file not found: {filename}, generating...")
        generate_default_settings(filename)

    with open(filename, 'r') as file:
        settings = toml.load(file)
    return settings

def generate_default_settings(filename):
    """Generate default settings and save to a TOML file."""
    default_settings = {
        'server': {
            'host': '',
            'port': '25575',
            'password': ''
        }
    }
    with open(filename, 'w') as file:
        toml.dump(default_settings, file)

def validate_server_settings(settings):
    """Validate server settings."""
    host = settings.get('server', {}).get('host')
    port = settings.get('server', {}).get('port')
    password = settings.get('server', {}).get('password')
    if not all([host, port, password]):
        print("配置文件不完整，请填写所有的服务器配置信息。")
        print("Configuration file is incomplete. Please fill in all server configuration information.")
        host = input("服务器地址Server address: ")
        # port = input("服务器端口：Server port: ") 默认25575
        password = input("RCON 密码RCON password: ")
        settings['server'] = {'host': host, 'port': port, 'password': password}
        try:
            port = int(port)  # Convert port to integer
            with open("config\config.toml", 'w') as file:
                toml.dump(settings, file)
            return True
        except:
            return False
    return True


def validate_command(command):
    """Validate user command."""
    if not command.strip():
        print("命令不能为空。")
        print("Command cannot be empty.")
        return False
    return True

def connect_to_server(settings):
    """Connect to the Minecraft server using the settings."""
    host = settings['server']['host']
    port = int(settings['server']['port'])  # Convert port to integer
    password = settings['server']['password']
    if port != 25575:
        print("端口号不是默认的 25575，请检查是否正确。")
        print("The port number is not the default 25575, please check if it is correct.")
    return MCRcon(host, password, port)


def load_players(file_path):
    """Load joined players from a file."""
    try:
        with open(file_path, 'r') as file:
            joined_players = file.read().splitlines()
        return joined_players
    except FileNotFoundError:
        print(f"未找到文件：{file_path}，正在生成...")
        print(f"File not found: {file_path}, generating...")
        with open(file_path, 'w') as file:
            file.write("")
        return []

def explain_op(op):
    """Remove Minecraft formatting codes from a string."""
    ops = re.sub('§.?','',op)
    return ops

def main():
    """Main function to execute."""
    settings_file = r"config\config.toml"
    players_file = r'joined_players.txt'

    settings = load_settings(settings_file)

    if not validate_server_settings(settings):
        return



    if not os.path.exists(players_file):
        print(f"未找到玩家列表文件：{players_file}，正在生成...")
        print(f"Players list file not found: {players_file}, generating...")
        with open(players_file, 'w') as file:
            file.write("")

    player_list = load_players(players_file)
    if player_list: 
        print("玩家列表：Players List:", ', '.join(player_list))
    rcon = connect_to_server(settings)
    A = input("是否输入指令？(Y/N) Enter command? (Y/N): ")
    if A.lower() == 'y':
        A = True
    else:
        A = False
    if not A:
        print("quit")
    while A:
        rcon.connect()
        command = input("请输入要执行的命令Enter command to execute: ")
        if not validate_command(command):
            continue
        ops = rcon.command(command)
        op = ops
        ops = explain_op(op)
        print("输出结果Output:", ops)
        rcon.disconnect()
        print("输入exit退出 Enter 'exit' to quit")

if __name__ == '__main__':
    main()
