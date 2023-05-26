import ctypes
import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import pandas.io.clipboard as cb

def windowTitle():
    projectName = "信手 StickyBoard"
    version = ' v 1.0'
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

    # 打开text.txt，将其所有内容按行分开，然后存放在列表中
    with open('text.txt','r', encoding= "utf-8") as f:
        element = f.readlines()
    for i in element:
        if i == "\n":
            element.remove(i)
    # element的类型是列表

    # 文本框，支持多选
    container = tk.Listbox(window,
                            selectmode = 'extended',
                            width=600,
                            height=100)
    for item in element:
        # 最开始所有元素是倒序排列的，因为原代码会把每一项排第一个位置：
        # container.insert(0,item)
        container.insert(tk.END,item)

    # 某人的Python大作业同款滚动条
    container.VScroll1 = tk.Scrollbar(window, orient = 'vertical')
    container.VScroll1.pack(side = "right", fill = "y")
    container.config(yscrollcommand = container.VScroll1.set)
    container.VScroll1.config(command = container.yview)
    container.pack()

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
    # menu.add_cascade(label='复制',
    #                 command=lambda:copyToClipboard())
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
