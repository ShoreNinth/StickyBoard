# StickyBoard
StickyBoard（信手）是一个类便签小工具，可能有点用。

> 厌倦了手指在C键和V键来回移动的繁琐？你需要StickyBoard！

> ~~差距？差距就是抽纸与卷纸的差距！~~

# 灵感
我需要一个理想应用：既能像便利贴那样置顶，又能像剪切板那样单击即复制。

于是，StickyBoard诞生。其英文名用StickyNote(便利贴)和Clipboard(剪切板)拼接而成，中文名“信手”取自成语“信手拈来”。

~~这个应用是写着玩的~~

我会尽力维护这个软件，有问题欢迎提issue。

不管怎样，希望这个小工具有些用。至少...嗯，能减少你按Ctrl+C的次数。

# 功能

## StickyBoard for Windows

~~读取同目录下的text.txt(编码默认UTF-8，如果没有请自行创建)，按行分割文本。~~
选择任意文本文件（支持代码文件，编码为UTF-8），按行分割文本。

单击即复制所选中行的内容。

窗口可置顶。

## StickyBoard for Linux(敬请期待)

### StickyBoard for Gnome

🚧🚧🚧施工中🚧🚧🚧

将StickyBoard移植到Gnome桌面。

### StickyBoard for KDE plasma 

🚧🚧🚧施工中🚧🚧🚧

KDE plasma的桌面自带剪切板。除了不能拖动外，其他功能可以代替StickyBoard。为此我准备了一个命令行版本。

它可以读取目标文本文件，并逐行复制，与KDE剪切板联动。

# 自行编译

可能需要额外下载的库有:pandas，tkinter

使用以下命令安装：

```
pip install pandas
pip install tkinter
```

# 感谢
Microsoft New Bing ~~必应大小姐~~

Google Bard

OpenAI ChatGPT
