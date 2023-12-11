# StickyBoard for Linux Gnome DE

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class metaData():
    global appName
    global author
    global isBeta
    global isCanary
    global version

    appName = "StickyBoard"
    # appIcon = "icon.ico"
    version = 'v1.2'
    isBeta = False
    isCanary = False
    author = "ShoreNinth"
    website = "https://github.com/ShoreNinth/StickyBoard"
    websiteLabel = "访问官网"

    appVersion = "版本：" + version
    if isCanary == True:
        appEdition = "金丝雀版"
    elif isBeta == True:
        appEdition = "测试版"
    else:
        appEdition = "稳定版"

    aboutString = appVersion + appEdition + "\nMade with GTK"

class mainWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title=appName)
        self.set_default_size(800, 600)

        box = Gtk.Box(spacing=6)
        self.add(box)


        aboutButton = Gtk.Button(label="关于")
        aboutButton.connect("clicked", self.about_page)
        box.add(aboutButton)

        # menuButton = Gtk

    def about_page(self, widget):

        about_dialog = Gtk.AboutDialog()
        about_dialog.set_program_name(appName)
        # about_dialog.set_logo_icon_name(metaData.appIcon)
        about_dialog.set_version(metaData.aboutString)
        about_dialog.set_authors([author])
        about_dialog.set_website(metaData.website)
        about_dialog.set_website_label(metaData.websiteLabel)
        about_dialog.run()
        about_dialog.destroy()


window = mainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()