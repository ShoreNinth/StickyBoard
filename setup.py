# StickyBoard Pyinstaller 打包助手
# StickyBoard Pyinstaller BuildWizard
import os
import sys

version = '1.1'

Language=os.environ.get('LANGUAGE')

print(
    "  ______         _         _             ______                            _ "+ "\n" +
    "/  _____)   _   (_)       | |           (____  \                          | |"+ "\n" +
    "( (____   _| |_  _   ____ | |  _  _   _  ____)  )  ___   _____   ____   __| |"+ "\n" +
    " \____ \ (_   _)| | / ___)| |_/ )| | | ||  __  (  / _ \ (____ | / ___) / _  |"+ "\n" +
    " _____) )  | |_ | |( (___ |  _ ( | |_| || |__)  )| |_| |/ ___ || |    ( (_| |"+ "\n" +
    "(______/    \__)|_| \____)|_| \_) \__  ||______/  \___/ \_____||_|     \____|"+ "\n" +
    "                                  (____/                                     "+ "\n"
    )
print(
    "______         _  _      _   _    _  _                        _ "+ "\n"+
    "| ___ \       (_)| |    | | | |  | |(_)                      | |"+ "\n"+
    "| |_/ / _   _  _ | |  __| | | |  | | _  ____  __ _  _ __   __| |"+ "\n"+
    "| ___ \| | | || || | / _` | | |/\| || ||_  / / _` || '__| / _` |"+ "\n"+
    "| |_/ /| |_| || || || (_| | \  /\  /| | / / | (_| || |   | (_| |"+ "\n"+
    "\____/  \__,_||_||_| \__,_|  \/  \/ |_|/___| \__,_||_|    \__,_|"+ "\n"
    )

class InfoText():
    Title_zh_CN = "StickyBoard Pyinstaller 打包助手"
    Version_zh_CN = "版本：" + version

    Title_en_US="StickyBoard Pyinstaller BuildWizard"
    Version_en_US="Version："+version

    Option_zh_CN="1.为Windows构建\n"+"2.构建Linux GTK版\n"+"3.构建Linux Qt版\n"+"4.构建Windows Qt版\n"+"5.退出\n"
    Option_en_US="1.Build for Windows\n"+"2.Build for Linux GTK\n"+"3.Build for Linux Qt\n"+"4.Build for Windows Qt\n"+"5.Exit\n"


if Language == "zh_CN":
    print(InfoText.Title_zh_CN)
    print(InfoText.Version_zh_CN)
else:
    print(InfoText.Title_en_US)
    print(InfoText.Version_en_US)

windows_prefix = "pyinstaller -F -w -i icon.ico "

main = "main.py"
qt = "qt.py"

buildForWindows = windows_prefix+main
buildQtForWindows = windows_prefix+qt

if Language == "zh_CN":
    print(InfoText.Option_zh_CN)
else:
    print(InfoText.Option_en_US)

promptList=[1,2,3,4,5]

loopLock = 1

while(loopLock==1):
    prompt = int(input('请输入序号：'))

    if prompt in promptList:
        loopLock=0
    else:
        print("输入序号错误，请重新输入。")

    if prompt == 1:
        os.system(buildForWindows)
    elif prompt == 2:
        print("敬请期待")
        pass
    elif prompt == 3:
        print("敬请期待")
        pass
    elif prompt == 4:
        os.system(buildQtForWindows)
    elif prompt == 5:
        sys.exit()