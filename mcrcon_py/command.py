from mcrcon import MCRcon
import toml

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

# 从文件加载玩家列表
def load_joined_players(filename):
    with open(filename, 'r', encoding='gbk') as file:
        joined_players = file.read().splitlines()
    return joined_players

def change_game_mode(rcon, joined_players):
    mode = input("请输入要切换的游戏模式：可选择的模式有：'creative', 'survival', 'adventure', 'spectator'")
    print('请输入要切换的玩家名字：')
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    name = input()
    rcon.connect()
    rcon.command(f'gamemode {mode} {name}')
    rcon.disconnect()    
    
def teleport_player(rcon,joined_players):
    
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    target_player = input("请输入要传送的玩家名字：")
    destination = input("请输入目标位置坐标（格式：x y z）：")
    rcon.connect()
    rcon.command(f'tp {target_player} {destination}')
    rcon.disconnect()
def give_item(rcon,joined_players):
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    target_player = input("请输入要给予物品的玩家名字：")
    with open(r"mcrcon_py\linux\id.txt", 'r',encoding='utf-8') as file:
        id_list = file.read().splitlines()
    print(f"物品ID列表：{id_list}")
    item_id = input("请输入物品ID：")
    count = input("请输入物品数量：")
    rcon.connect()
    rcon.command(f'give {target_player} {item_id} {count}')
    rcon.disconnect()
def kill_player(rcon,joined_players):
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    target_player = input("请输入要杀死的玩家名字：")
    rcon.connect()
    rcon.command(f'kill {target_player}')
    rcon.disconnect()
def ban_player(rcon,joined_players):
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    target_player = input("请输入要封禁的玩家名字：")
    rcon.connect()
    rcon.command(f'ban {target_player}')
    rcon.disconnect()
def unban_player(rcon,joined_players):
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    target_player = input("请输入要解封的玩家名字：")
    rcon.connect()
    rcon.command(f'pardon {target_player}')
    rcon.disconnect()
def kick_player(rcon,joined_players):
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    target_player = input("请输入要踢出的玩家名字：")
    rcon.connect()
    rcon.command(f'kick {target_player}')
    rcon.disconnect()
def switch_difficulty(rcon,joined_players):
    rcon.connect()
    difficulty = input("请输入要设置的难度：'peaceful', 'easy', 'normal', 'hard'")
    rcon.command(f'difficulty {difficulty}')
    rcon.disconnect()
def switch_gamerule(rcon,joined_players):
    rcon.connect()
    rule = input("请输入要设置的规则：")
    value = input("请输入要设置的值：")
    rcon.command(f'gamerule {rule} {value}')
    rcon.disconnect()
def switch_whitelist(rcon,joined_players):
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    rcon.connect()
    action = input("请输入要执行的操作：'on', 'off', 'list', 'add', 'remove'")
    if action == 'list':
        print(rcon.command('whitelist list'))
    else:
        player = input("请输入要操作的玩家名字：")
        rcon.command(f'whitelist {action} {player}')
    rcon.disconnect()
def switch_op(rcon,joined_players):
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    rcon.connect()
    player = input("请输入要操作的玩家名字：")
    action = input("请输入要执行的操作：'list', 'add', 'remove'")
    if action == 'list':
        rcon.command('op list')
        print(rcon.command('op list'))
    elif action == 'add':
        ops = rcon.command(f'op {player}')
        print("成功", ops)
    elif action == 'remove':
        ops = rcon.command(f'deop {player}')
        print("成功", ops)
    rcon.disconnect()
def switch_weather(rcon,joined_players):
    rcon.connect()
    weather = input("请输入要设置的天气：'storm', 'sun'")
    time = input("请输入要设置的时间：")
    rcon.command(f'weather world {weather} {time}')
    rcon.disconnect()

def switch_time(rcon,joined_players):
    rcon.connect()
    time = input("请输入要设置的时间：")
    rcon.command(f'time set {time}')
    rcon.disconnect()
def switch_banlist(rcon,joined_players):
    print(f"目前的玩家列表：{', '.join(joined_players)}")
    rcon.connect()
    action = input("请输入要执行的操作：'ips', 'players', 'list', 'add', 'remove'")
    if action == 'list':
        rcon.command('banlist list')
        print(rcon.command('banlist list'))
    else:
        player = input("请输入要操作的玩家名字：")
        rcon.command(f'banlist {action} {player}')
    rcon.disconnect()

# 定义可执行指令列表
commands = {
    '1': change_game_mode,
    '2': teleport_player,
    '3': give_item,
    '4': kill_player,
    '5': ban_player,
    '6': unban_player,
    '7': kick_player,
    '8': switch_weather,
    '9': switch_time,
    '10': switch_difficulty,
    '11': switch_gamerule,
    '12': switch_whitelist,
    '13': switch_op,
    '14': switch_banlist,
    'exit': None  # 退出命令
}
#config\config.toml
settings = load_settings(r"config\config.toml")
rcon = connect_to_server(settings)

# 从文件加载玩家列表
joined_players = load_joined_players(r"joined_players.txt")

print("下面是一些可用的命令：")
print("1. 切换游戏模式")
print("2. 传送玩家")
print("3. 给予玩家物品")
print("4. 杀死玩家")
print("5. 封禁玩家")
print("6. 解封玩家")
print("7. 踢出玩家")
print("8. 设置天气")
print("9. 设置时间")
print("10. 设置难度")
print("11. 设置游戏规则")
print("12. 管理白名单")
print("13. 管理操作员")
print("14. 管理封禁名单")
print("你是否想使用这些命令？确认请输入'True'")
bool_setting = input()
if bool_setting == 'True':
    while True:
        print("可用的命令：", ', '.join(commands.keys()))
        print("请输入要执行的命令：输入'exit'退出程序")
        setting = input()
        if setting in commands:
            if setting == 'exit':
                break
            else:
                commands[setting](rcon, joined_players)
                print('执行成功')
        else:
            print("无效命令，请重新输入。")
else:
    print("不使用命令")