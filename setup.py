# StickyBoard Pyinstaller 打包助手
import os

version = '1.1'

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

print("StickyBoard Pyinstaller 打包助手")
print("版本："+version)

windows_prefix = "pyinstaller -F -w -i icon.ico "

main = "main.py"
qt = "qt.py"

buildForWindows = windows_prefix+main
buildQtForWindows = windows_prefix+qt

print("1.为Windows构建\n"+
      "2.为Gnome Linux构建\n"
      +"3.为KDE Linux构建\n"
      +"4.构建Windows Qt版\n")
promptList=[1,2,3,4]

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