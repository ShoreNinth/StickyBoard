# StickyBoard Inporter Edition Cli
# 面向KDE的命令行版本
# 将文本文件导入剪切板

def messageShow():
    print("这是个饼，敬请期待")

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
    projectName = "信手 StickyBoard"
    version = 'v1.2'
    isBeta = False
    isCanary = True
    author = 'ShoreNinth'

    info = projectName + " " + version + " by " + author

    if isBeta == True:
        info += " Beta"
    if isCanary == True:
        info += " Canary"

    print(info)

def fileOperation():
    """文件操作"""
    # 选择文件
    fileSelected = tkinter.filedialog.askopenfilename(title = "选择文件")
    with open(fileSelected, 'r', encoding= "utf-8") as f:
        element = f.readlines()
    # 移除空行
    element = [i.strip() for i in element if i.strip()]


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
    miscDetails =  "github.com/ShoreNinth\n"

    aboutString = appName + "\n" + appVersion +appEdition+"\n" + appAuthor + "\n" + miscDetails

    return aboutString


if __name__ == "__main__":
    infoShow()
    messageShow()
    