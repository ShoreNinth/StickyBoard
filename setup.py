# StickyBoard 打包助手
import os

version = '1.0'

print("StickyBoard 打包助手")
print("版本："+version)

buildForWindows = "pyinstaller -F -w -i icon.ico main.py"

print("1.为Windows构建\n"+
      "2.为Gnome Linux构建\n"
      +"3.为KDE Linux构建\n")

prompt = int(input('请输入序号：'))

if prompt == 1:
    os.system(buildForWindows)
elif prompt == 2:
    print("敬请期待")
    pass
elif prompt == 3:
    print("敬请期待")
    pass
