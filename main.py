# StickyBoard for Windows
import ctypes
import tkinter as tk
import tkinter.filedialog
import tkinter.ttk
import tkinter.messagebox
import pandas.io.clipboard as cb

def windowTitle():

    projectName = "信手 StickyBoard"
    version = ' v1.1 Canary'
    author = ' by ShoreNinth'
    return projectName + version + author

def windowShow():

    window = tk.Tk()
    window.geometry('800x600')
    window.title(windowTitle())

    # 适配高DPI
    try:  # >= win 8.1
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except:  # win 8.0 or less
        ctypes.windll.user32.SetProcessDPIAware()
    ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    window.tk.call('tk', 'scaling', ScaleFactor/75)

    # 文本框，支持多选
    container = tk.Listbox(window,
                            selectmode = 'extended',
                            width=600,
                            height=100)

    element=""

    def elementInsert():
        for item in element:
            # 最开始所有元素是倒序排列的，因为原代码会把每一项排第一个位置：
            # container.insert(0,item)
            container.insert(tk.END,item)
        print('elementInsert执行成功')

    # 某人的Python大作业同款滚动条
        container.VScroll1 = tk.Scrollbar(window, orient = 'vertical')
        container.VScroll1.pack(side = "right", fill = "y")
        container.config(yscrollcommand = container.VScroll1.set)
        container.VScroll1.config(command = container.yview)
        container.pack()

    def fileOperation():
        # 选择文件
        f_path = tkinter.filedialog.askopenfilename(title = "选择文件")
        fileSelevted = f_path
        with open(fileSelevted, 'r', encoding= "utf-8") as f:
            element = f.readlines()
        # 移除空行
        for i in element:
            if i == "\n":
                element.remove(i)
        # element的类型是列表
        elementInsert()

    # 暂时弃用删除功能
    # def delete():
    #     # 删除选中项，方案来自谷歌Bard
    #     if not container.curselection():
    #         tk.messagebox.showinfo("提示", "请选择要删除的文本")
    #     else:
    #         for index in container.curselection():
    #             container.delete(index)

    def topWinOrUndo():
        # 窗口置顶与否，方案来自谷歌Bard
        if window.wm_attributes("-topmost"):
            window.wm_attributes("-topmost", False)
        else:
            window.wm_attributes("-topmost", True)

    def instandCopy(self):
        """Bard的建议。当没选中东西时不复制内容。可能有用？"""
        if not container.curselection():
            return
        item=""
        for i in container.curselection():
            item += container.get(i) + "\n"
        cb.copy(item)

    container.bind("<ButtonRelease-1>",instandCopy)

    # def copyToClipboard():
    #     # 方案来自New Bing
    #     content = ""
    #     for index in container.curselection():
    #         content += container.get(index) + "\n"
    #     cb.copy(content)

        # 旧代码：在选择多行时会报错
        # content=container.get(container.curselection())
        # cb.copy(content)

    menu = tk.Menu(window)
    menu.add_cascade(label='打开文件',
                     command=lambda:fileOperation())
    # menu.add_cascade(label='删除',
    #                 command=lambda:delete())
    menu.add_cascade(label='置顶窗口/取消置顶',
                    command=lambda:topWinOrUndo())
    menu.add_cascade(label='关于',
                    command=lambda:tk.messagebox.showinfo("关于","作者：ShoreNinth\ngithub.com/ShoreNinth\nMade with Tkinter"))                                   
 
    window.config(menu=menu)
    window.mainloop()

if __name__ == "__main__":
    windowTitle()
    windowShow()
