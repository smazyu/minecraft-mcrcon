模块介绍：
automation_linux.py：
这个模块用于自动监控当前玩家数量，并在新玩家进入时发送欢迎信息。同时，它还负责每隔 30 分钟清理一次世界掉落物。
command.py：
提供了通过 mcrcon 执行的常见命令，用于与游戏服务器进行交互。
一键开服.bat：
提供了一键开启游戏服务器的脚本，您只需要修改核心文件的名称即可开始使用。
Visualization.py：
通过可视化界面，您可以直观地管理游戏服务器，包括添加白名单、封禁玩家、踢出玩家等功能。此模块读取当前玩家列表文件，方便选择要管理的玩家。
main_automation.py：
实现了与 automation_linux.py 相同的功能，但启用时会自动打开可视化界面，提供更便捷的管理方式。
附加文件：
id.txt：
包含常见物品的 ID，当您执行给予物品的命令时，会自动打开此文件以提供物品列表。
使用说明：
使用 automation_linux.py 或 main_automation.py 监控服务器状态和自动执行清理任务。
使用 command.py 执行游戏服务器的常见命令。
使用 Visualization.py 进行可视化管理，操作更直观、便捷。
功能概览
MCRcon 服务器管理工具 (Python 脚本)
main_automation.py：
发送欢迎消息给新玩家
定时清理地面物品
监控玩家的加入和退出
同时打开Minecraft 服务器管理工具
Minecraft 服务器管理工具 GUI (Python 程序)

切换游戏模式
传送玩家
给予玩家物品
杀死玩家
封禁和解封玩家
设置天气和时间
设置难度和游戏规则
管理白名单、操作员和封禁名单
Minecraft 服务器管理命令行工具 (Python 程序)
切换游戏模式
传送玩家
给予玩家物品
杀死玩家
封禁和解封玩家
踢出玩家
设置天气和时间
设置难度和游戏规则
管理白名单、操作员和封禁名单
Minecraft 服务器一键启动脚本 (Windows 批处理脚本)
一键启动 Minecraft 服务器
自动分配内存
可选择 Java 版本
使用说明
安装依赖
在运行任何工具之前，请确保已安装以下依赖：
bash
pip install mcrcon toml
配置文件
在配置工具之前，请确保已配置好对应的配置文件，包含了 Minecraft 服务器的相关信息。
运行工具
MCRcon 服务器管理工具：
运行 main.py 文件启动 MCRcon 服务器管理工具。
若要启动数据可视化程序，运行 Visualization.py 文件。
Minecraft 服务器管理工具 GUI：
运行 main.py 文件启动 GUI 程序。
Minecraft 服务器管理命令行工具：
运行 main.py 文件启动命令行程序。
Minecraft 服务器一键启动脚本：
双击运行 start_server.bat 文件即可启动 Minecraft 服务器。
执行操作
根据对应工具的界面或命令行提示，输入相应的信息来执行操作。
注意事项
在执行任何操作之前，请确保已正确连接到 Minecraft 服务器，并且输入的信息是准确的，否则可能会导致意外的结果。
如果在使用过程中遇到任何问题，请及时联系管理员进行解决。

如有任何问题或建议，欢迎联系管理员。

