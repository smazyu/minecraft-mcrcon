import toml
from mcrcon import MCRcon

def load_settings(filename):
    with open(filename, 'r') as file:
        settings = toml.load(file)
    return settings

def connect_to_server(settings):
    host = settings['server']['host']
    port = settings['server']['port']
    password = settings['server']['password']
    return MCRcon(host, password, port)

def load_players(file_path):
    try:
        with open(file_path, 'r') as file:
            joined_players = file.read().splitlines()
        return joined_players
    except FileNotFoundError:
        return []

def main():
    settings = load_settings(r"config\config.toml")
    rcon = connect_to_server(settings)
    file_path = r'joined_players.txt'
    player_list = load_players(file_path)
    if player_list:
        print(f"玩家列表：{', '.join(player_list)}")
    A = input("是否输入指令？(Y/N)")
    if A.lower() == 'y':
        A = True
    else:
        A = False
    while A:
        rcon.connect()
        command = input("请输入要执行的命令：")
        ops = rcon.command(command)
        print(ops)
        rcon.disconnect()
        print("输入exit退出")
        B = input("是否继续输入指令？(Y/N)")
        if B.lower() == 'y':
            A = True
        else:
            A = False

if __name__ == '__main__':
    main()
