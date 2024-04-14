# 模块介绍

- **automation_linux.py：** 用于自动监控当前玩家数量，并在新玩家进入时发送欢迎信息。同时，负责每隔 30 分钟清理一次世界掉落物。
  
- **command.py：** 提供通过 mcrcon 执行的常见命令，用于与游戏服务器进行交互。
  
- **一键开服.bat：** 提供一键开启游戏服务器的脚本，只需修改核心文件的名称即可开始使用。
  
- **Visualization.py：** 通过可视化界面直观地管理游戏服务器，包括添加白名单、封禁玩家、踢出玩家等功能。该模块读取当前玩家列表文件，方便选择要管理的玩家。
  
- **main_automation.py：** 实现与 automation_linux.py 相同功能，但启用时会自动打开可视化界面，提供更便捷的管理方式。

- **quickly_command.py：** 提供自动化由服务器自动化管理工具生成的玩家列表，在对话框内输入指令(如你在游戏内输入op指令一样)

### 附加文件

- **id.txt：** 包含常见物品的 ID，当执行给予物品的命令时，command.py 会自动打开此文件提供物品列表。

# 使用说明

- 使用 automation_linux.py 或 main_automation.py 监控服务器状态和自动执行清理任务。
  
- 使用 command.py 执行游戏服务器的常见命令。
  
- 使用 Visualization.py 进行可视化管理，操作更直观、便捷。

- 使用一键开服.bat 快速启动游戏服务器。

- 使用 quickly_command.py 远程输入指令，无须登入游戏和终端

- log文件夹下会存储错误详细

# 功能概览

## MCRcon 服务器自动化管理工具 (Python 脚本)

- **main_automation.py：**
  - 发送欢迎消息给新玩家
  - 定时清理地面物品
  - 监控玩家的加入和退出
  - 同时打开 Minecraft 服务器管理工具 GUI

**注意：** 若您不想自动启动 GUI 程序，请使用 automation_linux.py 或 automation_win.py 文件。

## Minecraft 服务器管理工具 GUI (Python 程序)

- **Visualization.py：**
  - 提供可视化界面
  - 功能包括：
    - 切换游戏模式
    - 传送玩家
    - 给予玩家物品
    - 杀死玩家
    - 封禁和解封玩家
    - 设置天气和时间
    - 设置难度和游戏规则
    - 管理白名单、操作员和封禁名单

**注意：** 若您不需要可视化界面，请使用 command.py 文件。

## Minecraft 服务器管理命令行工具 (Python 程序)

- **command.py：**
  - 切换游戏模式
  - 传送玩家
  - 给予玩家物品
  - 杀死玩家
  - 封禁和解封玩家
  - 踢出玩家
  - 设置天气和时间
  - 设置难度和游戏规则
  - 管理白名单、操作员和封禁名单

## Minecraft 服务器一键启动脚本 (Windows 批处理脚本)

- **一键开服.bat：**
  - 一键启动 Minecraft 服务器
  - 自动分配内存
  - 可选择 Java 版本
  - 可选择核心文件，只需修改核心文件的名称即可开始使用

## Minecraft MCRCON 快速指令 (Python 程序)
- **quickly_command.py：**
  - 提供自动化由服务器自动化管理工具生成的玩家列表
  - 在对话框内输入指令(如你在游戏内输入op指令一样)
### 安装依赖

在运行任何工具之前，请确保已安装以下依赖：
```bash
pip install mcrcon toml
```
# 注意事项

## 配置文件

- 在使用工具之前，请确保已配置好对应的配置文件，包含了 Minecraft 服务器的相关信息。

## 运行工具

- **MCRcon 服务器管理工具：**
  - 运行 automation_win.py 或 automation_linux.py 文件启动 MCRcon 服务器自动化管理工具。
  - 若要自动启动服务器管理工具 GUI，请使用 main_automation.py 文件。

- **Minecraft 服务器管理工具 GUI：**
  - 运行 Visualization.py 文件启动 GUI 程序。

- **Minecraft 服务器管理命令行工具：**
  - 运行 command.py 文件启动命令行程序。

- **Minecraft 服务器一键启动脚本：**
  - 双击运行 一键开服.bat 文件即可启动 Minecraft 服务器。

- **Minecraft MCRCON 快速指令 (Python 程序)：**
  - 运行 quickly_command.py 文件启动命令行程序
## 执行操作

根据对应工具的界面或命令行提示，输入相应的信息来执行操作。

## 配置 mcrcon

- 在使用之前，请确保在 Minecraft 服务器的世界属性中打开了 mcrcon。如果您使用了 Paper 端或其他服务器端，请确保在世界属性中打开了 mcrcon 的同时也在 Paper 端的默认设置中打开。如果您使用的是其他核心，请在该核心的开发者文档中找到对应的设置，并进行开启。

## 路径更改

- 若您并非下载了整个项目，请在使用前更改路径。特别注意，可视化程序的玩家选择是基于自动化程序生成的玩家列表。

## Bug 报告和问题反馈

- 如果程序存在 bug 或您有任何问题，请及时联系管理员。我乐意帮助您解决问题。

## 欢迎联系管理员

- 如果您有任何问题或建议，欢迎随时联系管理员。我愿意提供支持并听取您的意见。

---

因为本人作为大一学生，精力有限，如果您愿意提供帮助，非常欢迎您的加入。





