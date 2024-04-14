import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
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

# 切换游戏模式
def change_game_mode():
    mode = mode_var.get()
    player = player_var.get()
    rcon.connect()
    rcon.command(f'gamemode {mode} {player}')
    rcon.disconnect()
    messagebox.showinfo("成功", "游戏模式切换成功。")

# 传送玩家
def teleport_player():
    target_player = target_player_var.get()
    destination = destination_var.get()
    rcon.connect()
    rcon.command(f'tp {target_player} {destination}')
    rcon.disconnect()
    messagebox.showinfo("成功", "玩家传送成功。")

# 给予玩家物品
def give_item():
    target_player = target_player_item_var.get()
    item_id = item_id_var.get()
    count = count_var.get()
    rcon.connect()
    rcon.command(f'give {target_player} {item_id} {count}')
    rcon.disconnect()
    messagebox.showinfo("成功", "物品给予成功。")

# 杀死玩家
def kill_player():
    target_player = target_player_kill_var.get()
    rcon.connect()
    rcon.command(f'kill {target_player}')
    rcon.disconnect()
    messagebox.showinfo("成功", "玩家被杀死。")

# 封禁玩家
def ban_player():
    target_player = target_player_ban_var.get()
    rcon.connect()
    rcon.command(f'ban {target_player}')
    rcon.disconnect()
    messagebox.showinfo("成功", "玩家已被封禁。")

# 解封玩家
def unban_player():
    target_player = target_player_unban_var.get()
    rcon.connect()
    rcon.command(f'pardon {target_player}')
    rcon.disconnect()
    messagebox.showinfo("成功", "玩家已解封。")

# 踢出玩家
def kick_player():
    target_player = target_player_kick_var.get()
    rcon.connect()
    rcon.command(f'kick {target_player}')
    rcon.disconnect()
    messagebox.showinfo("成功", "玩家已被踢出。")

# 设置天气
def switch_weather():
    weather = weather_var.get()
    time = time_weather_var.get()
    rcon.connect()
    rcon.command(f'weather world {weather} {time}')
    rcon.disconnect()
    messagebox.showinfo("成功", f"天气设置为{weather},时间为{time}。")

# 设置时间
def switch_time():
    time = time_var.get()
    rcon.connect()
    rcon.command(f'time set {time}')
    rcon.disconnect()
    messagebox.showinfo("成功", "时间设置成功。")

# 设置难度
def switch_difficulty():
    difficulty = difficulty_var.get()
    rcon.connect()
    rcon.command(f'difficulty {difficulty}')
    rcon.disconnect()
    messagebox.showinfo("成功", "难度设置成功。")

# 设置游戏规则
def switch_gamerule():
    rule = rule_var.get()
    value = value_var.get()
    rcon.connect()
    rcon.command(f'gamerule {rule} {value}')
    rcon.disconnect()
    messagebox.showinfo("成功", "游戏规则设置成功。")

# 管理白名单
def switch_whitelist():
    action = whitelist_action_var.get()
    player = player_var_whitelist .get()
    rcon.connect()
    if action == 'list':
        whitelist = rcon.command('whitelist list')
        messagebox.showinfo("白名单列表", whitelist)
    else:
        rcon.command(f'whitelist {action} {player}')
        messagebox.showinfo("成功", f"玩家已被{action}白名单。")
    rcon.disconnect()

# 管理操作员
def switch_op():
    action = op_action_var.get()
    player = player_var_op.get()
    rcon.connect()
    if action == 'list':
        ops = rcon.command('op list')
        messagebox.showinfo(" 响应", ops)
    elif action == 'add':
        ops = rcon.command(f'op {player}')
        messagebox.showinfo("成功", ops)
    elif action == 'remove':
        ops = rcon.command(f'deop {player}')
        messagebox.showinfo("成功", ops)
    rcon.disconnect()

# 管理封禁名单
def switch_banlist():
    action = banlist_action_var.get()
    player = target_player_ban_var.get()
    rcon.connect()
    if action == 'list':
        banlist = rcon.command('banlist list')
        messagebox.showinfo("封禁名单列表", banlist)
    else:
        rcon.command(f'banlist {action} {player}')
        messagebox.showinfo("成功", f"玩家已被{action}封禁名单。")
    rcon.disconnect()

root = tk.Tk()
root.title("Minecraft 服务器管理")

# 加载设置并连接服务器
settings = load_settings(r"\minecraft-mcrcon\config\config.toml")
rcon = connect_to_server(settings)
joined_players = load_joined_players(r"\minecraft-mcrcon\joined_players.txt")

# 创建滚动条
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建一个带滚动条的框架
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=5)
main_frame.grid_columnconfigure(0, weight=1)  # 自动调整列宽以适应滚动条

# 将滚动条绑定到框架
canvas = tk.Canvas(main_frame, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=canvas.yview)

# 创建另一个帧以包含所有部件
second_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=second_frame, anchor='nw')

# 添加所有部件到第二个帧

# 切换游戏模式
change_game_mode_frame = tk.LabelFrame(second_frame, text="切换游戏模式")
change_game_mode_frame.pack(padx=10, pady=5)
mode_var = tk.StringVar()
player_var = tk.StringVar()
tk.Label(change_game_mode_frame, text="游戏模式：").grid(row=0, column=0, padx=5, pady=5)
tk.OptionMenu(change_game_mode_frame, mode_var, 'creative', 'survival', 'adventure', 'spectator').grid(row=0, column=1, padx=5, pady=5)
tk.Label(change_game_mode_frame, text="玩家：").grid(row=1, column=0, padx=5, pady=5)
player_dropdown = ttk.Combobox(change_game_mode_frame, textvariable=player_var, values=joined_players)
player_dropdown.grid(row=1, column=1, padx=5, pady=5)
player_dropdown.set("选择玩家")
tk.Button(change_game_mode_frame, text="切换游戏模式", command=change_game_mode).grid(row=2, columnspan=2, padx=5, pady=5)

# 传送玩家
teleport_player_frame = tk.LabelFrame(second_frame, text="传送玩家")
teleport_player_frame.pack(padx=10, pady=5)
target_player_var = tk.StringVar()
destination_var = tk.StringVar()
tk.Label(teleport_player_frame, text="玩家：").grid(row=0, column=0, padx=5, pady=5)
player_dropdown_teleport = ttk.Combobox(teleport_player_frame, textvariable=target_player_var, values=joined_players)
player_dropdown_teleport.grid(row=0, column=1, padx=5, pady=5)
player_dropdown_teleport.set("选择玩家")
tk.Label(teleport_player_frame, text="目的地坐标：").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(teleport_player_frame, textvariable=destination_var).grid(row=1, column=1, padx=5, pady=5)
tk.Button(teleport_player_frame, text="传送玩家", command=teleport_player).grid(row=2, columnspan=2, padx=5, pady=5)

# 给予玩家物品
give_item_frame = tk.LabelFrame(second_frame, text="给予玩家物品")
give_item_frame.pack(padx=10, pady=5)
target_player_item_var = tk.StringVar()
item_id_var = tk.StringVar()
count_var = tk.StringVar()
tk.Label(give_item_frame, text="玩家：").grid(row=0, column=0, padx=5, pady=5)
player_dropdown_give = ttk.Combobox(give_item_frame, textvariable=target_player_item_var, values=joined_players)
player_dropdown_give.grid(row=0, column=1, padx=5, pady=5)
player_dropdown_give.set("选择玩家")
tk.Label(give_item_frame, text="物品ID：").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(give_item_frame, textvariable=item_id_var).grid(row=1, column=1, padx=5, pady=5)
tk.Label(give_item_frame, text="数量：").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(give_item_frame, textvariable=count_var).grid(row=2, column=1, padx=5, pady=5)
tk.Button(give_item_frame, text="给予物品", command=give_item).grid(row=3, columnspan=2, padx=5, pady=5)

# 杀死玩家
kill_player_frame = tk.LabelFrame(second_frame, text="杀死玩家")
kill_player_frame.pack(padx=10, pady=5)
target_player_kill_var = tk.StringVar()
tk.Label(kill_player_frame, text="玩家：").grid(row=0, column=0, padx=5, pady=5)
player_dropdown_kill = ttk.Combobox(kill_player_frame, textvariable=target_player_kill_var, values=joined_players)
player_dropdown_kill.grid(row=0, column=1, padx=5, pady=5)
player_dropdown_kill.set("选择玩家")
tk.Button(kill_player_frame, text="杀死玩家", command=kill_player).grid(row=1, columnspan=2, padx=5, pady=5)

# 封禁玩家
ban_player_frame = tk.LabelFrame(second_frame, text="封禁玩家")
ban_player_frame.pack(padx=10, pady=5)
target_player_ban_var = tk.StringVar()
tk.Label(ban_player_frame, text="玩家：").grid(row=0, column=0, padx=5, pady=5)
player_dropdown_ban = ttk.Combobox(ban_player_frame, textvariable=target_player_ban_var, values=joined_players)
player_dropdown_ban.grid(row=0, column=1, padx=5, pady=5)
player_dropdown_ban.set("选择玩家")
tk.Button(ban_player_frame, text="封禁玩家", command=ban_player).grid(row=1, columnspan=2, padx=5, pady=5)

# 解封玩家
unban_player_frame = tk.LabelFrame(second_frame, text="解封玩家")
unban_player_frame.pack(padx=10, pady=5)
target_player_unban_var = tk.StringVar()
tk.Label(unban_player_frame, text="玩家：").grid(row=0, column=0, padx=5, pady=5)
player_dropdown_unban = ttk.Combobox(unban_player_frame, textvariable=target_player_unban_var, values=joined_players)
player_dropdown_unban.grid(row=0, column=1, padx=5, pady=5)
player_dropdown_unban.set("选择玩家")
tk.Button(unban_player_frame, text="解封玩家", command=unban_player).grid(row=1, columnspan=2, padx=5, pady=5)

# 踢出玩家
kick_player_frame = tk.LabelFrame(second_frame, text="踢出玩家")
kick_player_frame.pack(padx=10, pady=5)
target_player_kick_var = tk.StringVar()
tk.Label(kick_player_frame, text="玩家：").grid(row=0, column=0, padx=5, pady=5)
player_dropdown_kick = ttk.Combobox(kick_player_frame, textvariable=target_player_kick_var, values=joined_players)
player_dropdown_kick.grid(row=0, column=1, padx=5, pady=5)
player_dropdown_kick.set("选择玩家")
tk.Button(kick_player_frame, text="踢出玩家", command=kick_player).grid(row=1, columnspan=2, padx=5, pady=5)

# 设置天气
switch_weather_frame = tk.LabelFrame(second_frame, text="设置天气")
switch_weather_frame.pack(padx=10, pady=5)

weather_var = tk.StringVar()
tk.Label(switch_weather_frame, text="天气：").grid(row=0, column=0, padx=5, pady=5)
tk.OptionMenu(switch_weather_frame, weather_var, 'storm', 'sun').grid(row=0, column=1, padx=5, pady=5)

time_weather_var = tk.StringVar()
tk.Label(switch_weather_frame, text="时间：").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(switch_weather_frame, textvariable=time_weather_var).grid(row=1, column=1, padx=5, pady=5)

tk.Button(switch_weather_frame, text="设置天气", command=switch_weather).grid(row=2, columnspan=2, padx=5, pady=5)



# 设置时间
switch_time_frame = tk.LabelFrame(second_frame, text="设置时间")
switch_time_frame.pack(padx=10, pady=5)
time_var = tk.StringVar()
tk.Label(switch_time_frame, text="时间：").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(switch_time_frame, textvariable=time_var).grid(row=0, column=1, padx=5, pady=5)
tk.Button(switch_time_frame, text="设置时间", command=switch_time).grid(row=1, columnspan=2, padx=5, pady=5)

# 设置难度
switch_difficulty_frame = tk.LabelFrame(second_frame, text="设置难度")
switch_difficulty_frame.pack(padx=10, pady=5)
difficulty_var = tk.StringVar()
tk.Label(switch_difficulty_frame, text="难度：").grid(row=0, column=0, padx=5, pady=5)
tk.OptionMenu(switch_difficulty_frame, difficulty_var, 'peaceful', 'easy', 'normal', 'hard').grid(row=0, column=1, padx=5, pady=5)
tk.Button(switch_difficulty_frame, text="设置难度", command=switch_difficulty).grid(row=1, columnspan=2, padx=5, pady=5)

# 设置游戏规则
switch_gamerule_frame = tk.LabelFrame(second_frame, text="设置游戏规则")
switch_gamerule_frame.pack(padx=10, pady=5)
rule_var = tk.StringVar()
value_var = tk.StringVar()
tk.Label(switch_gamerule_frame, text="规则：").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(switch_gamerule_frame, textvariable=rule_var).grid(row=0, column=1, padx=5, pady=5)
tk.Label(switch_gamerule_frame, text="值：").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(switch_gamerule_frame, textvariable=value_var).grid(row=1, column=1, padx=5, pady=5)
tk.Button(switch_gamerule_frame, text="设置游戏规则", command=switch_gamerule).grid(row=2, columnspan=2, padx=5, pady=5)

# 管理白名单
switch_whitelist_frame = tk.LabelFrame(second_frame, text="管理白名单")
switch_whitelist_frame.pack(padx=10, pady=5)
whitelist_action_var = tk.StringVar()
player_var_whitelist = tk.StringVar()
tk.Label(switch_whitelist_frame, text="操作：").grid(row=0, column=0, padx=5, pady=5)
tk.OptionMenu(switch_whitelist_frame, whitelist_action_var, 'on', 'off', 'list', 'add', 'remove').grid(row=0, column=1, padx=5, pady=5)
tk.Label(switch_whitelist_frame, text="玩家：").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(switch_whitelist_frame, textvariable=player_var_whitelist).grid(row=1, column=1, padx=5, pady=5)
tk.Button(switch_whitelist_frame, text="执行操作", command=switch_whitelist).grid(row=2, columnspan=2, padx=5, pady=5)

# 管理操作员
switch_op_frame = tk.LabelFrame(second_frame, text="管理操作员")
switch_op_frame.pack(padx=10, pady=5)
op_action_var = tk.StringVar()
player_var_op = tk.StringVar()
tk.Label(switch_op_frame, text="操作：").grid(row=0, column=0, padx=5, pady=5)
tk.OptionMenu(switch_op_frame, op_action_var, 'list', 'add', 'remove').grid(row=0, column=1, padx=5, pady=5)
tk.Label(switch_op_frame, text="玩家：").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(switch_op_frame, textvariable=player_var_op).grid(row=1, column=1, padx=5, pady=5)
tk.Button(switch_op_frame, text="执行操作", command=switch_op).grid(row=2, columnspan=2, padx=5, pady=5)

# 管理封禁名单
switch_banlist_frame = tk.LabelFrame(second_frame, text="管理封禁名单")
switch_banlist_frame.pack(padx=10, pady=5)
banlist_action_var = tk.StringVar()
player_var_banlist = tk.StringVar()
tk.Label(switch_banlist_frame, text="操作：").grid(row=0, column=0, padx=5, pady=5)
tk.OptionMenu(switch_banlist_frame, banlist_action_var, 'ips', 'players', 'list', 'add', 'remove').grid(row=0, column=1, padx=5, pady=5)
tk.Label(switch_banlist_frame, text="玩家：").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(switch_banlist_frame, textvariable=player_var_banlist).grid(row=1, column=1, padx=5, pady=5)
tk.Button(switch_banlist_frame, text="执行操作", command=switch_banlist).grid(row=2, columnspan=2, padx=5, pady=5)

# 更新框架大小以适应内容
second_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
