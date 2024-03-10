# StickyBoard Qt

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def windowTitle():

    global author
    global isBeta
    global isCanary
    global version
    global filetype_error_dialog
    
    projectName = "信手 StickyBoard"
    version = 'v1.2'
    isBeta = False
    isCanary = False
    author = 'ShoreNinth'
    filetype_error_dialog = '错误: 不受支持的文件格式'
    return projectName

class MyListWidget(QtWidgets.QListWidget):
    def clicked(self, item):
        QtWidgets.QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

class Ui_MainWindow(object):
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
        self.statusbar.showMessage("就绪")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
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


    def fileOperation():
        """文件操作"""
        element=""
        # 选择文件
        try:
            # fileSelected = QtWidgets.QFileDialog.askopenfilename(title = "选择文件")
            fileSelected = 'text.txt'
            with open(fileSelected, 'r', encoding= "utf-8") as f:
                element = f.readlines()
            # 移除空行
            element = [i.strip() for i in element if i.strip()]
            # 插入列表
            for item in element:
                ui.listWidget.addItem(item)

        # 如果目标文件不可读取，则弹窗报错
        except UnicodeDecodeError:
            QtWidgets.QMessageBox.information(title='提示',text=filetype_error_dialog)
    # def statusSituation(self):

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # 此方法在选择文件时调用
    Ui_MainWindow.fileOperation()

    MainWindow.show()
    sys.exit(app.exec_())
