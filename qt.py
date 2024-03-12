# StickyBoard Qt

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class metaInfo():

    projectName = "信手 StickyBoard"
    version = 'v1.3'
    isCanary = True
    isBeta = True
    author = 'ShoreNinth'
    filetype_error_dialog = '错误: 不受支持的文件格式'

    appName = "StickyBoard Qt"
    appVersion = "版本："+version+" "
    appAuthor = "作者："+author
    miscDetails =  "github.com/ShoreNinth\n"+"Made with PyQt5"
    appTitle = appName

    if isCanary == True:
        appEdition = "金丝雀版"
        appTitle += " Canary"
    elif isBeta == True:
        appEdition = "测试版"
        appTitle += " Beta"
    else:
        appEdition = "稳定版"

    aboutString = appName + "\n" + appVersion + appEdition+"\n" + appAuthor + "\n" + miscDetails

class MyListWidget(QtWidgets.QListWidget):
    def clicked(self,item):
        Clipboard.instantCopy(item.text())

class Clipboard():
    def instantCopy(self):
        """复制选中内容"""
        cb = QtWidgets.QApplication.clipboard()
        cb.setText(self)

class MessageBox():
    def filetypeError(self):
        QtWidgets.QMessageBox.information(self,'提示',metaInfo.filetype_error_dialog)

    def aboutMessageBox():
        QtWidgets.QMessageBox.information(None,'关于',str(metaInfo.aboutString))

class Ui_MainWindow(QtWidgets.QTextBrowser):

    statusbar = '就绪'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAcceptDrops(True)

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
        self.action.setShortcut("CTRL+O")
        self.action.triggered.connect(fileOperation.fileSelection)

        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.setShortcut("CTRL+H")
        self.action_2.triggered.connect(MessageBox.aboutMessageBox)

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
        MainWindow.setWindowTitle(_translate("MainWindow", metaInfo.appTitle))

        self.menu.setTitle(_translate("MainWindow", "打开"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "文件"))
        self.action_2.setText(_translate("MainWindow", "关于"))

    def dragEnterEvent(self, event):
        print("sss")
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.statusbar.showMessage('拖放文件以打开')

    def dropEvent(self, event):
        print("sss")
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith('.txt'):  # 确保文件是文本文件
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.setText(file.read())
                    self.statusbar.showMessage('成功打开文件：' + file_path)
                    return
        self.statusbar.showMessage('拖放的文件不是文本文件或不受支持')


class fileOperation():
    def fileSelection():
        """文件选择"""

        fileSelected = QtWidgets.QFileDialog.getOpenFileName()
        fileSelected = fileSelected[0]
        fileOperation.fileIsEmpty(fileSelected)

    def fileIsEmpty(file):
        """文件操作"""

        Ui_MainWindow.statusbar = '正在打开' + file

        if file == '':
            pass
        else:
            fileOperation.fileOpen(file)

    def fileOpen(file):
        element=""
        try:
            with open(file, 'r', encoding= "utf-8") as f:
                element = f.readlines()
            element = [i.strip() for i in element if i.strip()]
            # 插入列表
            ui.listWidget.clear
            for item in element:
                ui.listWidget.addItem(item)

            Ui_MainWindow.statusbar = '成功打开' + file
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
