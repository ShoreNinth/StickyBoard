# StickyBoard Digestor Edition
# 面向KDE的命令行版本
# 将文本文件导入剪切板
import pyperclip
import sys

def Arg():
    try:
        input = sys.argv[1]
    except IndexError:
        print("未指定文件")
        sys.exit()

    if input == '-h':
        print(aboutPage())
    else:
        try:
            fileOperation(input)
        except FileNotFoundError:
            print("文件不存在")
        except UnicodeDecodeError:
            print("此文件的格式不受支持")

def infoShow():

    print(
        "  ______         _         _             ______                            _ "+ "\n" +
        "/  _____)   _   (_)       | |           (____  \                          | |"+ "\n" +
        "( (____   _| |_  _   ____ | |  _  _   _  ____)  )  ___   _____   ____   __| |"+ "\n" +
        " \____ \ (_   _)| | / ___)| |_/ )| | | ||  __  (  / _ \ (____ | / ___) / _  |"+ "\n" +
        " _____) )  | |_ | |( (___ |  _ ( | |_| || |__)  )| |_| |/ ___ || |    ( (_| |"+ "\n" +
        "(______/    \__)|_| \____)|_| \_) \__  ||______/  \___/ \_____||_|     \____|"+ "\n" +
        "                                  (____/                                     "+ "\n"
        )

    global author
    global isBeta
    global isCanary
    global version 
    global edition

    projectName = "信手 StickyBoard"
    version = 'v1.2'
    edition = 'cli'
    isBeta = False
    isCanary = True
    author = 'ShoreNinth'

    info = projectName + " " + edition + " " + version

    if isBeta == True:
        info += " Beta"
    if isCanary == True:
        info += " Canary"

    print(info)
    print("使用-h参数查看版本")

def fileOperation(file):
    """文件操作"""
    # 选择文件
    fileSelected = file
    with open(fileSelected, 'r', encoding= "utf-8") as f:
        element = f.readlines()
    # 移除空行
    element = [i.strip() for i in element if i.strip()]
    for i in element:
        pyperclip.copy(i)
        print("已复制："+i)

def aboutPage():
    """关于页面"""
    appName = "StickyBoard for KDE plasma\n"
    appVersion = "版本："+version+" "
    if isCanary == True:
        appEdition = "金丝雀版"
    elif isBeta == True:
        appEdition = "测试版"
    else:
        appEdition = "稳定版"
    appAuthor = "作者："+author
    website =  "https://github.com/ShoreNinth\n"

    aboutString = appName + "\n" + appVersion +appEdition+"\n" + appAuthor + "\n" + website

    return aboutString


if __name__ == "__main__":
    infoShow()
    Arg()
    