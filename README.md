# ![图标](icon.ico "临时图标")StickyBoard

StickyBoard（信手）是一个文本复制工具。

⚠️警告：StickyBoard 仍在开发中，我不能保证它的安全性！

⚠️WIP Project! No warranty!

> "厌倦了手指在C键和V键来回移动的繁琐？你需要StickyBoard！"
> ——ShoreNinth

> ~~与直接操作TXT文件的差距？那就是抽纸与卷纸的差距！———ShoreNinth~~

# 灵感

我需要一个理想应用：既能像便利贴那样置顶，又能像剪切板那样单击即复制。 于是，StickyBoard诞生。

其英文名用StickyNote(便利贴)和Clipboard(剪切板)拼接而成，中文名“信手”取自成语“信手拈来”。

不管怎样，希望这个小工具有些用。至少...嗯，能减少你按Ctrl+C的次数。

# 计划面板

### 开发进度图例

| 图标 |   解释   |
| ---- | :------: |
| 🚧    |  未开始  |
| 💤    |   闲置   |
| 🧑‍💻    | 正在进行 |
| 🎉    |  已完成  |

## 🎉[StickyBoard Qt5](./qt.py)

使用PyQt5编写的前端。与旧版相比，加入了拖拽打开及快捷键的功能！

## 🧑‍💻[StickyBoard Qt6](./qt6.py)

为Qt6所准备的使用PyQt6编写的前端

## 🎉[StickyBoard (Legacy) for Windows](./main.py)

StickyBoard第一版，使用Tkinter构建。

从**2024年3月12日**起，Tkinter版将**不再**维护。请拥抱更先进的框架。

选择任意文本文件（支持代码文件，编码为UTF-8），此应用会按行分割文本。

单击即复制所选中行的内容。

应用窗口可置顶。

## 💤StickyBoard for Linux

## 💤[StickyBoard for Gnome](./Gnome.py)

使用GTK构建，让你有更舒适的Gnome桌面应用使用体验。

## 🧑‍💻[StickyBoard CLI for KDE plasma](./cli.py)

众所周知KDE plasma的桌面自带剪切板。除了不能拖动外，其他功能可以与StickyBoard相辅相成。为此我准备了一个命令行版本。它可以读取目标文本文件，并逐行复制，与KDE剪切板联动。

# 版本解释

在关于页面中，版本号右边显示了版本。

稳定版(Alpha)：是经过测试完全可用的版本

测试版(Beta)：有一些新功能，但存在bug

金丝雀版(Canary)：测试版中的测试版，拥有最新的功能和最多的Bug

# 自行编译

### 编译StickyBoard for Windows

下载pyinstaller库

```
pip install pyinstaller
```

克隆仓库

```
git clone https://github.com/ShoreNinth/StickyBoard.git
```

切换目录

```
cd StickyBoard
```

执行

```
python setup.py
```

### 编译StickyBoard for Linux

可能需要额外下载的库有:gi,pyinstaller。请使用以下命令安装：

```
sudo pip install -r requirements.txt
```
### 关于此图标

此软件的图标是从网上随便找的，在正式确定图标前以此图标![图标](icon.ico "临时图标")为主。


## Jetbrians

本项目已获得 [Jetbrians](https://github.com/JetBrains) 开源开发认证，感谢 Jetbrains 对开源软件的赞助。

