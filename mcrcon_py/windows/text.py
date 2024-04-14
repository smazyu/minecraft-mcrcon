from mcrcon import MCRcon
import toml
def connect_to_server(settings):
    host = settings['server']['host']
    port = settings['server']['port']
    password = settings['server']['password']
    return MCRcon(host, password, port)

def load_settings(filename):
    with open(filename, 'r') as file:
        settings = toml.load(file)
    return settings
settings = load_settings(r"\minecraft-mcrcon\config\config.toml")
rcon = connect_to_server(settings)

print("开始监听聊天消息...")
while True:
    rcon.connect()
    response = rcon.command('tellraw @a ["",{"text":"[Chat Recorder] 等待聊天消息...","color":"gray"}]')
    if response:
        message = response.strip()
        print(f"记录聊天消息: {message}")
    rcon.disconnect()
