# StickyBoard Qt

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# def windowTitle():

#     global author
#     global isBeta
#     global isCanary
#     global version
#     global filetype_error_dialog
    
#     projectName = "信手 StickyBoard"
#     version = 'v1.2'
#     isBeta = False
#     isCanary = False
#     author = 'ShoreNinth'
#     filetype_error_dialog = '错误: 不受支持的文件格式'
#     return projectName

class MyListWidget(QtWidgets.QListWidget):
    def clicked(self, item):
        QtWidgets.QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

class Clipboard():
    def instandCopy(self):
        """复制选中内容"""
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self)

class MessageBox():
    def filetypeError(self):
        QtWidgets.QMessageBox.information(self,'提示',Ui_MainWindow.filetype_error_dialog)

    def aboutMessageBox(self):
        QtWidgets.QMessageBox.information(self,'关于',Ui_MainWindow.aboutPage())

class Ui_MainWindow(object):

    projectName = "信手 StickyBoard"
    version = 'v1.2'
    isBeta = True
    isCanary = False
    author = 'ShoreNinth'
    filetype_error_dialog = '错误: 不受支持的文件格式'

    statusbar = '就绪'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.listWidget = MyListWidget()
        self.listWidget.itemClicked.connect(self.listWidget.clicked)
        self.scrollArea.setWidget(self.listWidget)

        self.gridLayout.addWidget(self.scrollArea, 0, 0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage(Ui_MainWindow.statusbar)

        MainWindow.setStatusBar(self.statusbar)

        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.triggered.connect(Ui_MainWindow.fileOperation)

        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.triggered.connect(MessageBox.aboutMessageBox)
        # self.action_2.triggered.connect(print(Ui_MainWindow.aboutPage()))

        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.gridLayout.addWidget(self.scrollArea, 0, 0)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StickyBoard"))

        self.menu.setTitle(_translate("MainWindow", "打开"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "文件"))
        self.action_2.setText(_translate("MainWindow", "关于"))


    def menuButtonTrigger(self):
        print('成功按下'+self)

    def aboutPage():
        """关于页面"""
        appName = "StickyBoard Qt\n"
        appVersion = "版本："+Ui_MainWindow.version+" "
        if Ui_MainWindow.isCanary == True:
            appEdition = "金丝雀版"
        elif Ui_MainWindow.isBeta == True:
            appEdition = "测试版"
        else:
            appEdition = "稳定版"
        appAuthor = "作者："+Ui_MainWindow.author
        miscDetails =  "github.com/ShoreNinth\n"+"Made with PyQt5"

        aboutString = appName + "\n" + appVersion +appEdition+"\n" + appAuthor + "\n" + miscDetails
        return aboutString


    def fileOperation():
        """文件操作"""

        element=""
        
        fileSelected = QtWidgets.QFileDialog.getOpenFileName()
        fileSelected = fileSelected[0]

        Ui_MainWindow.statusbar = '正在打开' + fileSelected

        if fileSelected == '':
            pass
        else:
            try:
                with open(fileSelected, 'r', encoding= "utf-8") as f:
                    element = f.readlines()
                element = [i.strip() for i in element if i.strip()]
                # 插入列表
                ui.listWidget.clear
                for item in element:
                    ui.listWidget.addItem(item)

                Ui_MainWindow.statusbar = '成功打开' + fileSelected
        # 如果目标文件不可读取，则弹窗报错
            except UnicodeDecodeError:
               MessageBox.filetypeError(None)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
