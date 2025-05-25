# StickyBoard Qt

# -*- coding: utf-8 -*-

from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class MetaInfo():
    projectName = "信手 StickyBoard"
    version = 'v1.3'
    isCanary = False
    isBeta = True
    author = 'ShoreNinth'
    filetype_error_dialog = '错误: 不受支持的文件格式'

    appName = "StickyBoard Qt"
    appVersion = "版本："+version+" "
    appAuthor = "作者："+author
    miscDetails =  "github.com/ShoreNinth\n"+"Made with PyQt6"
    appTitle = appName

    if isCanary == True:
        appEdition = "金丝雀版"
        appTitle += " Canary"
    elif isBeta == True:
        appEdition = "测试版"
        appTitle += " Beta"
    else:
        appEdition = "稳定版"

    aboutString = appName + "\n" + appVersion + appEdition + "\n" + appAuthor + "\n" + miscDetails

class MyListWidget(QtWidgets.QListWidget):
    def clicked(self, item: QtWidgets.QListWidgetItem):
        Clipboard.instantCopy(item.text())

class Clipboard():
    @staticmethod
    def instantCopy(text: str):
        """复制选中内容"""
        cb = QtWidgets.QApplication.clipboard()
        cb.setText(text)

class MessageBox():
    @staticmethod
    def filetypeError():
        QtWidgets.QMessageBox.information(None, '提示', MetaInfo.filetype_error_dialog)

    @staticmethod
    def aboutMessageBox():
        QtWidgets.QMessageBox.information(None, '关于', str(MetaInfo.aboutString))

class Ui_MainWindow(object):
    statusbarText = '就绪'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.listWidget = MyListWidget()

        global listwidget
        listwidget = self.listWidget

        self.listWidget.itemClicked.connect(self.listWidget.clicked)
        self.scrollArea.setWidget(self.listWidget)

        self.gridLayout.addWidget(self.scrollArea, 0, 0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")

        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage(Ui_MainWindow.statusbarText)

        MainWindow.setStatusBar(self.statusbar)

        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action.setShortcut(QtGui.QKeySequence.keyBindings(open))
        self.action.triggered.connect(FileOperation.fileSelection)

        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        # self.action_2.setShortcut(QtGui.QKeySequence.)
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
        MainWindow.setWindowTitle(_translate("MainWindow", MetaInfo.appTitle))

        self.menu.setTitle(_translate("MainWindow", "打开"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "文件"))
        self.action_2.setText(_translate("MainWindow", "关于"))

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            # self.statusbar.showMessage('拖放文件以打开')

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            FileOperation.fileOpen(file_path)
        # self.statusbar.showMessage('拖放的文件不是文本文件或不受支持')

class FileOperation():
    @staticmethod
    def fileSelection():
        """文件选择"""
        fileSelected, _ = QtWidgets.QFileDialog.getOpenFileName()
        FileOperation.fileIsEmpty(fileSelected)

    @staticmethod
    def fileIsEmpty(file):
        """文件操作"""
        Ui_MainWindow.statusbarText = '正在打开' + file
        if file == '':
            pass
        else:
            FileOperation.fileOpen(file)

    @staticmethod
    def fileOpen(file):
        element = ""
        try:
            with open(file, 'r', encoding="utf-8") as f:
                element = f.readlines()
            element = [i.strip() for i in element if i.strip()]
            for item in element:
                listwidget.addItem(item)
            Ui_MainWindow.statusbarText = '成功打开' + file
        except UnicodeDecodeError:
            MessageBox.filetypeError()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
