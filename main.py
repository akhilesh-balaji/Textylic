import tkinter
import os
import time
import getpass
import webbrowser
from tkinter import font
from random import randint
from tkinter import filedialog
from tkinter import PhotoImage

# Defining Window Properties
root = tkinter.Tk()
root.withdraw()
def mainWindow():
    window = tkinter.Toplevel()
    window.title("Notes window")
    window.attributes("-toolwindow", True)
    window.overrideredirect(1)
    window.geometry("306x306+" + str(randint(10, 900)) + "+" + str(randint(10, 500)))
    window.config(bg = "#333333")
    window.wait_visibility(window)
    window.grid_columnconfigure(0, weight = 1)
    window.grid_columnconfigure(1, weight = 1)
    window.grid_columnconfigure(2, weight = 100000)
    window.grid_columnconfigure(3, weight = 1000)
    window.grid_columnconfigure(4, weight = 0)
    window.grid_columnconfigure(5, weight = 0)
    window.grid_columnconfigure(6, weight = 0)

    # Getting opened file name
    global openedFileName
    openedFileName = False

    global saved
    saved = False

    # Tooltip Class
    class ToolTip(object):
        def __init__(self, widget):
            self.widget = widget
            self.tipwindow = None
            self.id = None
            self.x = self.y = 0

        def showtip(self, text):
            "Display text in tooltip window"
            self.text = text
            if self.tipwindow or not self.text:
                return
            x, y, cx, cy = self.widget.bbox("insert")
            cx = cx
            x = x + self.widget.winfo_rootx() + 27
            y = y + cy + self.widget.winfo_rooty() +17
            self.tipwindow = tw = tkinter.Toplevel(self.widget)
            tw.wm_overrideredirect(1)
            tw.wm_geometry("+%d+%d" % (x, y))
            label = tkinter.Label(tw, text=self.text, justify="left",
                        background="#e3e3e3", relief="solid", borderwidth=0,
                        font=("Segoe_UI", "8", "normal"))
            label.pack(ipadx=2)

        def hidetip(self):
            tw = self.tipwindow
            self.tipwindow = None
            if tw:
                tw.destroy()

    def CreateToolTip(widget, text):
        toolTip = ToolTip(widget)
        def enter(event):
            toolTip.showtip(text)
        def leave(event):
            toolTip.hidetip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)
        # Create new window function

    def createNewWindow(var=False):
        mainWindow()

    # Formatting Buttons

    def bolder(var=False):
        bold_font  = font.Font(notes, notes.cget("font"))
        bold_font.configure(weight="bold")

        notes.tag_configure("bold", font=bold_font)
        current_tags = notes.tag_names("sel.first")

        if "bold" in current_tags:
            notes.tag_remove("bold", "sel.first", "sel.last")
        else:
            notes.tag_add("bold", "sel.first", "sel.last")
        return "break"

    def italicizer(var=False):
        italic_font  = font.Font(notes, notes.cget("font"))
        italic_font.configure(slant="italic")

        notes.tag_configure("italic", font=italic_font)
        current_tags = notes.tag_names("sel.first")

        if "italic" in current_tags:
            notes.tag_remove("italic", "sel.first", "sel.last")
        else:
            notes.tag_add("italic", "sel.first", "sel.last")
        return "break"

    def codify(var=False):
        notes.tag_configure("code", font="Consolas 11")
        current_tags = notes.tag_names("sel.first")

        if "code" in current_tags:
            notes.tag_remove("code", "sel.first", "sel.last")
        else:
            notes.tag_add("code", "sel.first", "sel.last")
        return "break"

    def underliner(var=False):
        under_font  = font.Font(notes, notes.cget("font"))
        under_font.configure(underline=True)

        notes.tag_configure("underline", font=under_font)
        current_tags = notes.tag_names("sel.first")

        if "underline" in current_tags:
            notes.tag_remove("underline", "sel.first", "sel.last")
        else:
            notes.tag_add("underline", "sel.first", "sel.last")
        
        return "break"

    def strikethrough(var=False):
        strike_font  = font.Font(notes, notes.cget("font"))
        strike_font.configure(overstrike=True)

        notes.tag_configure("strikethrough", font=strike_font)
        current_tags = notes.tag_names("sel.first")

        if "strikethrough" in current_tags:
            notes.tag_remove("strikethrough", "sel.first", "sel.last")
        else:
            notes.tag_add("strikethrough", "sel.first", "sel.last")
        
        return "break"

    def bulletList():
        x = notes.selection_get()
        current_tags = notes.tag_names("sel.first")

        if '\n' not in x:
            if "bullet" not in current_tags:
                y = float(notes.index("sel.first"))
                z = float(notes.index("sel.last"))
                bullete = "\t•  " + str(x)
                notes.delete(y, z)
                notes.insert(y, bullete)
                l = len(bullete)
                l = notes.index(y + l)
                notes.tag_add("bullet", y, l)
            elif "bullet" in current_tags:
                y = float(notes.index("sel.first"))
                z = float(notes.index("sel.last"))
                selected = notes.selection_get()
                selected = str(selected)
                selected = selected.replace("\t•  ", "")
                notes.insert("sel.first", selected)
                notes.delete("sel.first", "sel.last")
                l = len(selected)
                l = notes.index(l)
                notes.tag_remove("bullet", y, l)
        elif '\n' in x:
            if "bullet" not in current_tags:
                y = float(notes.index("sel.first"))
                z = float(notes.index("sel.last"))
                select = notes.selection_get()
                bullete = select.replace("\n", "\n\t•  ")
                bullete = "\t•  " + str(bullete)
                notes.delete(str(y), str(z))
                notes.insert(y, bullete)
                l = len(bullete)
                l = notes.index(y + l)
                notes.tag_add("bullet", y, l)
            elif "bullet" in current_tags:
                y = float(notes.index("sel.first"))
                z = float(notes.index("sel.last"))
                selected = x.replace("\n\t•  ", "\n")
                selected = selected.replace("\t•  ", "")
                notes.insert("sel.first", selected)
                notes.delete("sel.first", "sel.last")
                l = len(selected)
                l = notes.index(l)
                notes.tag_remove("bullet", y, l)
        
        return "break"

    def strikeButtonText(var=False):
        f = font.Font(notes, notes.cget("font"))
        f.configure(overstrike=True)
        strikeThrough.configure(font=f)

    def link(var=False):
        global linked

        under_font  = font.Font(notes, notes.cget("font"))
        under_font.configure(underline=True)

        notes.tag_configure("link", font=under_font, foreground="#00AFEC")
        current_tags = notes.tag_names("sel.first")

        if "link" in current_tags:
            notes.tag_remove("link", "sel.first", "sel.last")
            linked = False
        else:
            notes.tag_add("link", "sel.first", "sel.last")
            linked = True
        return "break"

    def openLink(var=False):
        global linked
        if linked == True:
            global url
            url = notes.selection_get()
            webbrowser.open_new(url)
        return "break"

    # List that holds all items that have accent color
    accentItems = []

    # File Dialog
    def openFile(var=False):
        username = getpass.getuser()
        if not os.path.exists("C:/Users/{}/Documents/Textylic".format(username)):
            os.makedirs("C:/Users/{}/Documents/Textylic".format(username))
        noteFile = filedialog.askopenfilename(initialdir="C:/Users/{}/Documents/Textylic".format(username), title="Choose a note:", filetypes=(("Textylic file", "*.txtlyc"),))
        if noteFile:
            global openedFileName
            openedFileName = noteFile
        noteFile = open(noteFile, "r")
        read = noteFile.read()
        notes.delete("1.0", "end")
        notes.insert("end", read)
        noteFile.close()
        return "break"

    def saveNoteAs(var=False):
        username = getpass.getuser()
        noteFile = filedialog.asksaveasfilename(confirmoverwrite=False, defaultextension=".txtlyc", filetypes=(("Textylic file", "*.txtlyc"),), initialdir="C:/Users/{}/Documents/Textylic".format(username), title="Save your note:")
        if noteFile:
            global saved
            saved = True
            noteFile = open(noteFile, "w")
            noteFile.write(notes.get(1.0, "end"))
            noteFile.close()
        return "break"

    def saveNote(var=False):
        global openedFileName
        if openedFileName:
            noteFile = open(openedFileName, "w")
            noteFile.write(notes.get(1.0, "end"))
            noteFile.close()
        else:
            saveNoteAs()
        return "break"

    def windowdestroy(var=False):
        root.destroy()

    # Accent color functions
    def accentpink():
        for item in accentItems:
            item.configure(bg = "#EB8EC6", activebackground = "#DA7DB5")
        close_button.configure(bg = "#EB8EC6")
        title_bar.configure(bg = "#EB8EC6")
        window.update()

    def accentyellow():
        for item in accentItems:
            item.configure(bg = "#E6B905", activebackground = "#D1A804")
        close_button.configure(bg = "#E6B905")
        title_bar.configure(bg = "#E6B905")
        window.update()

    def accentgreen():
        for item in accentItems:
            item.configure(bg = "#65BA5A", activebackground = "#5EAE54")
        close_button.configure(bg = "#65BA5A")
        title_bar.configure(bg = "#65BA5A")
        window.update()

    def accentblue():
        for item in accentItems:
            item.configure(bg = "#59C0E7", activebackground = "#53B3D8")
        close_button.configure(bg = "#59C0E7")
        title_bar.configure(bg = "#59C0E7")
        window.update()

    # Defining Title Bar Elements
    title_bar = tkinter.Frame(window, relief = "flat", bg = "#E6B905")

    new = tkinter.Button(title_bar, text = "+", width = 3, height = 1, bd = 0, bg = "#E6B905", command = createNewWindow, activebackground = "#D1A804")
    new.grid(row = 0, column = 0, padx = 0, sticky = "W")
    CreateToolTip(new, "New Note")
    accentItems.append(new)

    # Save
    save = tkinter.Button(title_bar, text = "💾", width = 4, bd = 0, height = 1, bg = "#E6B905", pady = 4, activebackground = "#D1A804", command = saveNote)
    save.grid(row = 0, column = 1, padx = 0, sticky = "W")
    CreateToolTip(save, "Save Note")
    accentItems.append(save)

    # Link opening button
    openlink = tkinter.Button(title_bar, text = "🔗", width = 4, bd = 0, height = 1, bg = "#E6B905", pady = 4, command = openLink, activebackground = "#D1A804")
    openlink.grid(row = 0, column = 2, padx = 0, sticky = "W")
    CreateToolTip(openlink, "Open Selected Link")
    accentItems.append(openlink)

    # Notes Text widget container
    notesFrame = tkinter.Frame(window, relief = "flat", bg = "#333333", height = 200, width = 297)
    notesFrame.grid(row = 1, column = 0, columnspan = 5)

    # Main Text input
    notes = tkinter.Text(notesFrame, undo = True, font = "Segoe_Print 11", bg = "#333333", padx = 5, pady = 10, bd = 0, fg = "white", insertbackground = "white", relief = "flat", selectbackground = "#616161", wrap = "word", height = 12.5, width = 36, tabs = ("0.5c", "3c", "5c"))
    notes.grid(row = 0, column = 0, rowspan = 5, columnspan = 5)

    # Extra Menu
    menu = tkinter.Menubutton(title_bar, text = "⋮", width = 3, bd = 0, bg = "#E6B905", relief = "flat", pady = 4, activebackground = "#D1A804")
    menu.grid(row = 0, column = 3, padx = 0, sticky = "W")
    CreateToolTip(menu, "Other Options")
    accentItems.append(menu)

    menu.menu = tkinter.Menu(menu, tearoff = 0, bd = 0, relief = "solid", font = "Segoe_UI 9", bg = "#333333", activeborderwidth = 0, activebackground = "#404040", fg = "white", activeforeground = "white", selectcolor = "white")
    menu["menu"] = menu.menu

    menu.menu.add_command(label = "Choose theme:")
    menu.menu.add_radiobutton(label = "Blue", command = accentblue)
    menu.menu.add_radiobutton(label = "Yellow", command = accentyellow)
    menu.menu.add_radiobutton(label = "Green", command = accentgreen)
    menu.menu.add_radiobutton(label = "Pink", command = accentpink)
    menu.menu.add_separator()
    menu.menu.add_command(label = "Open Note", command = openFile)
    menu.menu.add_command(label = "Save Note", command = saveNote, accelerator = "(Ctr+s)")
    menu.menu.add_separator()
    menu.menu.add_command(label = "Undo", command = notes.edit_undo, accelerator = "(Ctr+z)")
    menu.menu.add_command(label = "Redo", command = notes.edit_redo, accelerator = "(Ctr+y)")
    menu.menu.add_command(label = "Quit", command = windowdestroy, accelerator = "(Ctr+q)")
    menu.menu.add_command(label = "Help/About")

    close_button = tkinter.Button(title_bar, text = "X", width = 5, bd = 0, height = 1, bg = "#E6B905", command = window.destroy, pady = 4, activebackground = "#E81123")
    close_button.grid(row = 0, column = 6, padx = 144, sticky = "E")
    CreateToolTip(new, "New Note")

    # Bottom formatting bar
    borderFrame = tkinter.Frame(window, height = 0.5, width = 2000000, pady = 10)
    borderFrame.grid(row = 2, column = 0, columnspan = 10, sticky = "W")

    bottom_bar = tkinter.Frame(window, relief = "flat", bg = "#333333", pady = 3)
    bottom_bar.grid(row = 3, column = 0, columnspan = 5, rowspan = 1, sticky = "W")

    bold = tkinter.Button(bottom_bar, text = "𝗕", width = 3, height = 1, bd = 0, bg = "#333333", command = bolder, pady = 4, activebackground = "#D1A804", fg = "white", padx = 3)
    bold.grid(row = 0, column = 1, padx = 0, sticky = "W")

    italic = tkinter.Button(bottom_bar, text = "𝘐", width = 3, bd = 0, height = 1, bg = "#333333", command = italicizer, pady = 4, activebackground = "#D1A804", fg = "white", padx = 3)
    italic.grid(row = 0, column = 2, padx = 0, sticky = "W")

    underline = tkinter.Button(bottom_bar, text = "U̲", width = 3, bd = 0, height = 1, bg = "#333333", pady = 4, command = underliner, activebackground = "#D1A804", fg = "white", padx = 3)
    underline.grid(row = 0, column = 3, padx = 0, sticky = "W")

    strikeThrough = tkinter.Button(bottom_bar, text = "ab", width = 3, bd = 0, height = 1, bg = "#333333", pady = 4, command = strikethrough, activebackground = "#D1A804", fg = "white", padx = 3)
    strikeThrough.grid(row = 0, column = 4, padx = 0, sticky = "W")
    strikeButtonText()

    bullet = tkinter.Button(bottom_bar, text = "• —", width = 3, bd = 0, height = 1, bg = "#333333", pady = 4, command = bulletList, activebackground = "#D1A804", fg = "white", padx = 3)
    bullet.grid(row = 0, column = 5, padx = 0, sticky = "W")

    code = tkinter.Button(bottom_bar, text = "</>", width = 4, bd = 0, height = 1, bg = "#333333", pady = 4, command = codify, activebackground = "#D1A804", fg = "white", padx = 3)
    code.grid(row = 0, column = 6, padx = 0, sticky = "W")


    # Positioning title bar and adding drag function
    title_bar.grid(row = 0, column = 0, columnspan = 5, sticky = "W")
    def get_pos(event):
        xwin = window.winfo_x()
        ywin = window.winfo_y()
        startx = event.x_root
        starty = event.y_root

        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event):
            window.geometry("306x306" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
            
        startx = event.x_root
        starty = event.y_root

        title_bar.bind('<B1-Motion>', move_window)
    title_bar.bind('<Button-1>', get_pos)
    notes.bind('<Control-Key-b>', bolder)
    notes.bind('<Control-Key-i>', italicizer)
    notes.bind('<Control-Key-u>', underliner)
    notes.bind('<Control-Key-t>', codify)
    notes.bind('<Control-Key-q>', windowdestroy)
    notes.bind('<Control-Key-s>', saveNote)
    notes.bind('<Control-Key-k>', link)
    notes.bind('<Control-Key-o>', openLink)
    notes.bind('<Control-slash>', strikethrough)

    # Autosave files
    # while True:
    #     saveNote()
    #     time.sleep(5)

    # Update the window

    # 💾

    window.mainloop()
mainWindow()