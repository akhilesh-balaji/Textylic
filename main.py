import tkinter
import pygetwindow as gw
import os
import time
import getpass
import webbrowser
import re
import tkinter.ttk
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
    window.geometry("310x310+" + str(randint(10, 900)) + "+" + str(randint(10, 500)))
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

    def createNewWindow(var=False):
        mainWindow()

    # Formatting Buttons

    def bolder(var=False):
        bold_font  = font.Font(notes, notes.cget("font"))
        bold_font.configure(weight="bold")

        italicBold_font  = font.Font(notes, notes.cget("font"))
        italicBold_font.configure(slant="italic", weight="bold")

        underBold_font  = font.Font(notes, notes.cget("font"))
        underBold_font.configure(underline=True, weight="bold")

        strikeBold_font  = font.Font(notes, notes.cget("font"))
        strikeBold_font.configure(overstrike=True, weight="bold")

        notes.tag_configure("bold", font=bold_font)
        notes.tag_configure("italicBold", font=italicBold_font)
        notes.tag_configure("underBold", font=underBold_font) 
        notes.tag_configure("strikeBold", font=strikeBold_font)               
        current_tags = notes.tag_names("sel.first")

        if "bold" in current_tags:
            notes.tag_remove("bold", "sel.first", "sel.last")
        elif "italicBold" in current_tags:
            notes.tag_remove("italicBold", "sel.first", "sel.last")
            notes.tag_add("italic", "sel.first", "sel.last")  
        elif "underBold" in current_tags:
            notes.tag_remove("underBold", "sel.first", "sel.last")
            notes.tag_add("underline", "sel.first", "sel.last")  
        elif "strikeBold" in current_tags:
            notes.tag_remove("strikeBold", "sel.first", "sel.last")  
            notes.tag_add("strikethrough", "sel.first", "sel.last")  
        else:
            if "italic" in current_tags:
                notes.tag_remove("italic", "sel.first", "sel.last")  
                notes.tag_add("italicBold", "sel.first", "sel.last")
            elif "underline" in current_tags:
                notes.tag_remove("underline", "sel.first", "sel.last")  
                notes.tag_add("underBold", "sel.first", "sel.last")
            elif "strikethrough" in current_tags:
                notes.tag_remove("strikethrough", "sel.first", "sel.last")  
                notes.tag_add("strikeBold", "sel.first", "sel.last")
            else:
                notes.tag_add("bold", "sel.first", "sel.last")
        return "break"

    def italicizer(var=False):
        italic_font  = font.Font(notes, notes.cget("font"))
        italic_font.configure(slant="italic")

        boldItalic_font  = font.Font(notes, notes.cget("font"))
        boldItalic_font.configure(slant="italic", weight="bold")

        underItalic_font  = font.Font(notes, notes.cget("font"))
        underItalic_font.configure(underline=True, slant="italic")

        strikeItalic_font  = font.Font(notes, notes.cget("font"))
        strikeItalic_font.configure(overstrike=True, slant="italic")

        notes.tag_configure("italic", font=italic_font)
        notes.tag_configure("boldItalic", font=boldItalic_font)
        notes.tag_configure("underItalic", font=underItalic_font) 
        notes.tag_configure("strikeItalic", font=strikeItalic_font) 
        current_tags = notes.tag_names("sel.first")

        if "italic" in current_tags:
            notes.tag_remove("italic", "sel.first", "sel.last")
        elif "boldItalic" in current_tags:
            notes.tag_remove("boldItalic", "sel.first", "sel.last")
            notes.tag_add("bold", "sel.first", "sel.last")  
        elif "underItalic" in current_tags:
            notes.tag_remove("underItalic", "sel.first", "sel.last")
            notes.tag_add("underline", "sel.first", "sel.last")  
        elif "strikeItalic" in current_tags:
            notes.tag_remove("strikeItalic", "sel.first", "sel.last") 
            notes.tag_add("strikethrough", "sel.first", "sel.last")  
        else:
            if "bold" in current_tags:
                notes.tag_remove("bold", "sel.first", "sel.last")  
                notes.tag_add("boldItalic", "sel.first", "sel.last") 
            elif "underline" in current_tags:
                notes.tag_remove("underline", "sel.first", "sel.last")  
                notes.tag_add("underItalic", "sel.first", "sel.last")
            elif "strikethrough" in current_tags:
                notes.tag_remove("strikethrough", "sel.first", "sel.last")  
                notes.tag_add("strikeItalic", "sel.first", "sel.last")
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

        boldUnder_font  = font.Font(notes, notes.cget("font"))
        boldUnder_font.configure(underline=True, weight="bold")

        italicUnder_font  = font.Font(notes, notes.cget("font"))
        italicUnder_font.configure(underline=True, slant="italic")

        strikeUnder_font  = font.Font(notes, notes.cget("font"))
        strikeUnder_font.configure(overstrike=True, underline=True)

        notes.tag_configure("underline", font=under_font)
        notes.tag_configure("boldUnder", font=boldUnder_font)
        notes.tag_configure("italicUnder", font=italicUnder_font) 
        notes.tag_configure("strikeUnder", font=strikeUnder_font)
        current_tags = notes.tag_names("sel.first")

        if "underline" in current_tags:
            notes.tag_remove("underline", "sel.first", "sel.last")
        elif "boldUnder" in current_tags:
            notes.tag_remove("boldUnder", "sel.first", "sel.last")
            notes.tag_add("bold", "sel.first", "sel.last")
        elif "italicUnder" in current_tags:
            notes.tag_remove("italicUnder", "sel.first", "sel.last")
            notes.tag_add("italic", "sel.first", "sel.last")
        elif "strikeUnder" in current_tags:
            notes.tag_remove("strikeUnder", "sel.first", "sel.last") 
            notes.tag_add("strikethrough", "sel.first", "sel.last")
        else:
            if "bold" in current_tags:
                notes.tag_add("boldUnder", "sel.first", "sel.last")
                notes.tag_remove("bold", "sel.first", "sel.last")  
            elif "italic" in current_tags:
                notes.tag_add("italicUnder", "sel.first", "sel.last")
                notes.tag_remove("italic", "sel.first", "sel.last")  
            elif "strikethrough" in current_tags:
                notes.tag_add("strikeUnder", "sel.first", "sel.last")
                notes.tag_remove("strikethrough", "sel.first", "sel.last")  
            else:
                notes.tag_add("underline", "sel.first", "sel.last")
        
        return "break"

    def strikethrough(var=False):
        strike_font  = font.Font(notes, notes.cget("font"))
        strike_font.configure(overstrike=True)

        boldStrike_font  = font.Font(notes, notes.cget("font"))
        boldStrike_font.configure(overstrike=True, weight="bold")

        italicStrike_font  = font.Font(notes, notes.cget("font"))
        italicStrike_font.configure(overstrike=True, slant="italic")

        underStrike_font  = font.Font(notes, notes.cget("font"))
        underStrike_font.configure(overstrike=True, underline=True)

        notes.tag_configure("strikethrough", font=strike_font)
        current_tags = notes.tag_names("sel.first")

        if "strikethrough" in current_tags:
            notes.tag_remove("strikethrough", "sel.first", "sel.last")
            notes.tag_add("strikethrough", "sel.first", "sel.last")
        elif "boldStrike" in current_tags:
            notes.tag_remove("boldStrike", "sel.first", "sel.last")
            notes.tag_add("bold", "sel.first", "sel.last")
        elif "italicStrike" in current_tags:
            notes.tag_remove("italicStrike", "sel.first", "sel.last")
            notes.tag_add("italic", "sel.first", "sel.last")
        elif "underStrike" in current_tags:
            notes.tag_remove("underStrike", "sel.first", "sel.last") 
            notes.tag_add("underline", "sel.first", "sel.last")
        else:
            if "bold" in current_tags:
                notes.tag_remove("bold", "sel.first", "sel.last")  
                notes.tag_add("boldStrike", "sel.first", "sel.last") 
            elif "italic" in current_tags:
                notes.tag_remove("italic", "sel.first", "sel.last")  
                notes.tag_add("italicStrike", "sel.first", "sel.last")
            elif "underline" in current_tags:
                notes.tag_remove("underline", "sel.first", "sel.last")  
                notes.tag_add("underStrike", "sel.first", "sel.last")
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

    # Change Text Color
    def setColor():
        global pinky
        global yellowy
        global greeny
        global bluey
        if yellowy == True:
            notes.tag_configure("emphColor", foreground="#E6B905")
        elif pinky == True:
            notes.tag_configure("emphColor", foreground="#EB8EC6")
        elif greeny == True:
            notes.tag_configure("emphColor", foreground="#65BA5A")
        elif bluey == True:
            notes.tag_configure("emphColor", foreground="#59C0E7")
        current_tags = notes.tag_names("sel.first")

        if "emphColor" in current_tags:
            notes.tag_remove("emphColor", "sel.first", "sel.last")
        else:
            notes.tag_add("emphColor", "sel.first", "sel.last")
        
        return "break"

    def openLink(var=False):
        global linked
        if linked == True:
            global url
            url = notes.selection_get()
            webbrowser.open_new(url)
        return "break"

    def openReadme(var=False):
        webbrowser.open_new("https://github.com/akhilesh-balaji/Textylic/blob/master/README.md")
        return "break"

    # Getting images (normal) for the buttons:
    global newButtonImage
    newButtonImage = PhotoImage(file = "images/iconset/new.png")

    global saveButtonImage
    saveButtonImage = PhotoImage(file = "images/iconset/save.png")

    global linkButtonImage
    linkButtonImage = PhotoImage(file = "images/iconset/open.png")

    global menuButtonImage
    menuButtonImage = PhotoImage(file = "images/iconset/menu.png")

    global closeButtonImage
    closeButtonImage = PhotoImage(file = "images/iconset/close.png")

    global boldButtonImage
    boldButtonImage = PhotoImage(file = "images/iconset/bold.png")

    global italicButtonImage
    italicButtonImage = PhotoImage(file = "images/iconset/italic.png")

    global underButtonImage
    underButtonImage = PhotoImage(file = "images/iconset/underline.png")

    global strikeButtonImage
    strikeButtonImage = PhotoImage(file = "images/iconset/strikethrough.png")

    global bulletButtonImage
    bulletButtonImage = PhotoImage(file = "images/iconset/bullet.png")

    global codeButtonImage
    codeButtonImage = PhotoImage(file = "images/iconset/code.png")

    global insertlButtonImage
    insertlButtonImage = PhotoImage(file = "images/iconset/link.png")

    global colorButtonImage
    colorButtonImage = PhotoImage(file = "images/iconset/color.png")

    # Getting images (hover) for the buttons:
    global newButtonImageAfter
    newButtonImageAfter = PhotoImage(file = "images/iconset/new1.png")

    global saveButtonImageAfter
    saveButtonImageAfter = PhotoImage(file = "images/iconset/save1.png")

    global linkButtonImageAfter
    linkButtonImageAfter = PhotoImage(file = "images/iconset/open1.png")

    global menuButtonImageAfter
    menuButtonImageAfter = PhotoImage(file = "images/iconset/menu1.png")

    global closeButtonImageAfter
    closeButtonImageAfter = PhotoImage(file = "images/iconset/close1.png")

    global boldButtonImageAfter
    boldButtonImageAfter = PhotoImage(file = "images/iconset/bold1.png")

    global italicButtonImageAfter
    italicButtonImageAfter = PhotoImage(file = "images/iconset/italic1.png")

    global underButtonImageAfter
    underButtonImageAfter = PhotoImage(file = "images/iconset/underline1.png")

    global strikeButtonImageAfter
    strikeButtonImageAfter = PhotoImage(file = "images/iconset/strikethrough1.png")

    global bulletButtonImageAfter
    bulletButtonImageAfter = PhotoImage(file = "images/iconset/bullet1.png")

    global codeButtonImageAfter
    codeButtonImageAfter = PhotoImage(file = "images/iconset/code1.png")

    global insertlButtonImageAfter
    insertlButtonImageAfter = PhotoImage(file = "images/iconset/link1.png")

    global colorButtonImageAfter
    colorButtonImageAfter = PhotoImage(file = "images/iconset/color1.png")

    # Changing the image on hover
    def hoverImageBold(var=False):
        bold.configure(image = boldButtonImageAfter)

    def NormalImageBold(var=False):
        bold.configure(image = boldButtonImage)
    
    def hoverImageItalic(var=False):
        italic.configure(image = italicButtonImageAfter)

    def NormalImageItalic(var=False):
        italic.configure(image = italicButtonImage)

    def hoverImageUnder(var=False):
        underline.configure(image = underButtonImageAfter)

    def NormalImageUnder(var=False):
        underline.configure(image = underButtonImage)

    def hoverImageStrike(var=False):
        strikeThrough.configure(image = strikeButtonImageAfter)

    def NormalImageStrike(var=False):
        strikeThrough.configure(image = strikeButtonImage)

    def hoverImageBullet(var=False):
        bullet.configure(image = bulletButtonImageAfter)

    def NormalImageBullet(var=False):
        bullet.configure(image = bulletButtonImage)

    def hoverImageCode(var=False):
        code.configure(image = codeButtonImageAfter)

    def NormalImageCode(var=False):
        code.configure(image = codeButtonImage)

    def hoverImageNew(var=False):
        new.configure(image = newButtonImageAfter)

    def NormalImageNew(var=False):
        new.configure(image = newButtonImage)

    def hoverImageSave(var=False):
        save.configure(image = saveButtonImageAfter)

    def NormalImageSave(var=False):
        save.configure(image = saveButtonImage)

    def hoverImageOpen(var=False):
        openlink.configure(image = linkButtonImageAfter)

    def NormalImageOpen(var=False):
        openlink.configure(image = linkButtonImage)

    def hoverImageMenu(var=False):
        menu.configure(image = menuButtonImageAfter)

    def NormalImageMenu(var=False):
        menu.configure(image = menuButtonImage)

    def hoverImageClose(var=False):
        close_button.configure(image = closeButtonImageAfter)

    def NormalImageClose(var=False):
        close_button.configure(image = closeButtonImage)

    def hoverImageLink(var=False):
        insertl.configure(image = insertlButtonImageAfter)

    def NormalImageLink(var=False):
        insertl.configure(image = insertlButtonImage)

    def hoverImageTsize(var=False):
        colorText.configure(image = colorButtonImageAfter)

    def NormalImageTsize(var=False):
        colorText.configure(image = colorButtonImage)

    # List that holds all items that have accent color
    accentItems = []

    # Get Tags
    def getTags(start, end):
        index = start
        tagname = []
        starttagindex = index
        prevtag = notes.tag_names(index)

        try:
           tagname.append([starttagindex, "end", notes.tag_names(index)])
        except:
           tagname.append([starttagindex, "end", ("",)])

        # def insertStingMiddle(string, word):
        #     strOriginal = string
        #     return string[:1] + word + strOriginal[1:]

        while notes.compare(index, "<", end):
            # print("Tag for text at index %s is %s" %(index, notes.tag_names(index)))
            # print(tagname)
            if notes.tag_names(index) != prevtag:
                if len(notes.tag_names(index)) <= 0:
                    starttagindex = index
                    legnth = len(tagname)
                    tagname[legnth - 1][1] = index
                    tagname.append([starttagindex, "end", ("",)])

                else:
                    starttagindex = index
                    legnth = len(tagname)
                    tagname[legnth - 1][1] = index
                    tagname.append([starttagindex, "end", notes.tag_names(index)])

            prevtag = notes.tag_names(index)
            index = notes.index(f"{index}+1c")
    
        return tagname

    # File Dialog
    def openFile(var=False):
        global saved
        noteFile = filedialog.askopenfilename(initialdir="./Notes", title="Choose a note:", filetypes=(("Textylic file", "*.txtlyc"),))
        if noteFile:
            global openedFileName
            openedFileName = noteFile
        noteFile = open(noteFile, "r")
        read = noteFile.read()

        matchStyle = re.match(r".*<style>\n(.*)\n</style>", str(read), flags=re.DOTALL|re.MULTILINE)

        read = re.sub('<style>.*</style>', '', read, flags=re.DOTALL|re.MULTILINE)
        read = re.sub('<content>\n', '', read, flags=re.DOTALL|re.MULTILINE)
        read = re.sub('\n</content>\n\n', '', read, flags=re.DOTALL|re.MULTILINE)

        notes.delete("1.0", "end")
        notes.insert("1.0", read)

        if matchStyle:
            # Bold fonts and tags
            formatting = matchStyle.group(1)
            formatting = eval(formatting)

            bold_font  = font.Font(notes, notes.cget("font"))
            bold_font.configure(weight="bold")

            italicBold_font  = font.Font(notes, notes.cget("font"))
            italicBold_font.configure(slant="italic", weight="bold")

            underBold_font  = font.Font(notes, notes.cget("font"))
            underBold_font.configure(underline=True, weight="bold")

            strikeBold_font  = font.Font(notes, notes.cget("font"))
            strikeBold_font.configure(overstrike=True, weight="bold")

            notes.tag_configure("bold", font=bold_font)
            notes.tag_configure("italicBold", font=italicBold_font)
            notes.tag_configure("underBold", font=underBold_font) 
            notes.tag_configure("strikeBold", font=strikeBold_font) 

            # Italic fonts and tags
            italic_font  = font.Font(notes, notes.cget("font"))
            italic_font.configure(slant="italic")

            boldItalic_font  = font.Font(notes, notes.cget("font"))
            boldItalic_font.configure(slant="italic", weight="bold")

            underItalic_font  = font.Font(notes, notes.cget("font"))
            underItalic_font.configure(underline=True, slant="italic")

            strikeItalic_font  = font.Font(notes, notes.cget("font"))
            strikeItalic_font.configure(overstrike=True, slant="italic")

            notes.tag_configure("italic", font=italic_font)
            notes.tag_configure("boldItalic", font=boldItalic_font)
            notes.tag_configure("underItalic", font=underItalic_font) 
            notes.tag_configure("strikeItalic", font=strikeItalic_font) 

            # Code font and tags
            notes.tag_configure("code", font="Consolas 11")

            # Underline font and tags
            under_font  = font.Font(notes, notes.cget("font"))
            under_font.configure(underline=True)

            boldUnder_font  = font.Font(notes, notes.cget("font"))
            boldUnder_font.configure(underline=True, weight="bold")

            italicUnder_font  = font.Font(notes, notes.cget("font"))
            italicUnder_font.configure(underline=True, slant="italic")

            strikeUnder_font  = font.Font(notes, notes.cget("font"))
            strikeUnder_font.configure(overstrike=True, underline=True)

            notes.tag_configure("underline", font=under_font)
            notes.tag_configure("boldUnder", font=boldUnder_font)
            notes.tag_configure("italicUnder", font=italicUnder_font) 
            notes.tag_configure("strikeUnder", font=strikeUnder_font)

            # Link font
            notes.tag_configure("link", font=under_font, foreground="#00AFEC")

            # Text color
            global pinky
            global yellowy
            global greeny
            global bluey
            if yellowy == True:
                notes.tag_configure("emphColor", foreground="#E6B905")
            elif pinky == True:
                notes.tag_configure("emphColor", foreground="#EB8EC6")
            elif greeny == True:
                notes.tag_configure("emphColor", foreground="#65BA5A")
            elif bluey == True:
                notes.tag_configure("emphColor", foreground="#59C0E7")

            # Apply formatting
            for format in formatting:
                for tag in format[2]:
                    notes.tag_add(str(tag).strip("}{/.\\"), format[0], format[1])

        noteFile.close()
        saved = True
        return "break"

    def saveNoteAs(var=False):
        global noteFile
        noteFile = filedialog.asksaveasfilename(confirmoverwrite=False, defaultextension=".txtlyc", filetypes=(("Textylic file", "*.txtlyc"),), initialdir="./Notes", title="Save your note:")
        if noteFile:
            global saved
            saved = True
            global openedFileName
            openedFileName = noteFile
            noteFile = open(noteFile, "w")
            noteFile.write(notes.get(1.0, "end"))
            noteFile.close()
        return "break"

    def saveNote(var=False):
        global saved
        global openedFileName
        if openedFileName:
            noteFile = open(openedFileName, "w")
            noteFile.write("<content>\n{}\n</content>\n\n".format(notes.get(1.0, "end")))
            noteFile.write("<style>\n{}\n</style>".format(getTags("1.0", "end")))
            noteFile.close()
            saved = True
            getTags("1.0", "end")
        else:
            saveNoteAs()
        return "break"

    def windowdestroy(var=False):
        root.destroy()

    # Accent color functions
    global pinky
    global yellowy
    global greeny
    global bluey
    pinky = False
    yellowy = True
    greeny = False
    bluey = False
    def accentpink():
        global pinky
        global yellowy
        global greeny
        global bluey
        pinky = True
        yellowy = False
        greeny = False
        bluey = False
        for item in accentItems:
            item.configure(bg = "#EB8EC6", activebackground = "#EB8EC6")
        title_bar.configure(bg = "#EB8EC6")
        menu.configure(activebackground = "#EB8EC6")
        notes.tag_configure("emphColor", foreground="#EB8EC6")
        window.update()

    def accentyellow():
        global pinky
        global yellowy
        global greeny
        global bluey
        pinky = False
        yellowy = True
        greeny = False
        bluey = False
        for item in accentItems:
            item.configure(bg = "#E6B905", activebackground = "#E6B905")
        title_bar.configure(bg = "#E6B905")
        notes.tag_configure("emphColor", foreground="#E6B905")
        menu.configure(activebackground = "#E6B905")
        window.update()

    def accentgreen():
        global pinky
        global yellowy
        global greeny
        global bluey
        pinky = False
        yellowy = False
        greeny = True
        bluey = False
        for item in accentItems:
            item.configure(bg = "#65BA5A", activebackground = "#65BA5A")
        title_bar.configure(bg = "#65BA5A")
        notes.tag_configure("emphColor", foreground="#65BA5A")
        menu.configure(activebackground = "#65BA5A")
        window.update()

    def accentblue():
        global pinky
        global yellowy
        global greeny
        global bluey
        pinky = False
        yellowy = False
        greeny = False
        bluey = True
        for item in accentItems:
            item.configure(bg = "#59C0E7", activebackground = "#59C0E7")
        title_bar.configure(bg = "#59C0E7")
        notes.tag_configure("emphColor", foreground="#59C0E7")
        menu.configure(activebackground = "#59C0E7")
        window.update()

    # Detecting TopOrNot
    def topOrNot():
        windows = gw.getActiveWindow()
        if windows is None:
            pass
        else:
            if windows.isMaximized:
                window.withdraw()
                window.attributes("-topmost", False)
            elif not windows.isMaximized and windows.title != '':
                window.attributes("-topmost", False)
            else:
                window.deiconify()
                window.lift()
                window.attributes("-topmost", True)

        window.after(10, topOrNot)

    # Auto save
    def autoSave():
        global saved
        if saved == True:
            saveNote()
        window.after(3000, autoSave)

    # Defining Title Bar Elements
    title_bar = tkinter.Frame(window, relief = "flat", bg = "#E6B905")

    new = tkinter.Button(title_bar, image = newButtonImage, bd = 0, bg = "#E6B905", command = createNewWindow, activebackground = "#E6B905")
    new.image = newButtonImage
    new.grid(row = 0, column = 0, padx = 5, sticky = "W", pady = 5)
    new.image = newButtonImage
    accentItems.append(new)

    # Save
    save = tkinter.Button(title_bar, image = saveButtonImage, bd = 0, bg = "#E6B905", pady = 4, activebackground = "#E6B905", command = saveNote)
    save.image = saveButtonImage
    save.grid(row = 0, column = 1, padx = 5, sticky = "W", pady = 5)
    accentItems.append(save)

    # Link opening button
    openlink = tkinter.Button(title_bar, image = linkButtonImage, bd = 0, bg = "#E6B905", pady = 4, command = openLink, activebackground = "#E6B905")
    openLink.image = linkButtonImage
    openlink.grid(row = 0, column = 2, padx = 5, sticky = "W", pady = 5)
    accentItems.append(openlink)

    # Notes Text widget container
    notesFrame = tkinter.Frame(window, relief = "flat", bg = "#333333", height = 200, width = 297)
    notesFrame.grid(row = 1, column = 0, columnspan = 5)

    # Main Text input
    notes = tkinter.Text(notesFrame, undo = True, font = "Segoe_Print 11", bg = "#333333", padx = 5, pady = 10, bd = 0, fg = "white", insertbackground = "white", relief = "flat", selectbackground = "#616161", wrap = "word", height = 12.5, width = 36, tabs = ("0.5c", "3c", "5c"))
    notes.grid(row = 0, column = 0, rowspan = 5, columnspan = 5)
    notes.delete("1.0", "end")

    # Extra Menu
    menu = tkinter.Menubutton(title_bar, image = menuButtonImage, bd = 0, bg = "#E6B905", relief = "flat", pady = 4, activebackground = "#E6B905")
    menu.image = menuButtonImage
    menu.grid(row = 0, column = 3, padx = 5, sticky = "W", pady = 5)
    accentItems.append(menu)

    menu.menu = tkinter.Menu(menu, tearoff = 0, bd = 0, relief = "solid", font = "Segoe_UI 9", activeborderwidth = 0, activebackground = "#c4c4c4", activeforeground = "#000000", selectcolor = "black")
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
    menu.menu.add_command(label = "Help/About", command = openReadme)

    close_button = tkinter.Button(title_bar, image = closeButtonImage, bd = 0, bg = "#E6B905", command = window.destroy, pady = 4, activebackground = "#E6B905")
    close_button.image = closeButtonImage
    close_button.grid(row = 0, column = 6, padx = 150, sticky = "E")
    accentItems.append(close_button)

    # Bottom formatting bar
    borderFrame = tkinter.Frame(window, height = 0.5, width = 2000000, pady = 10)
    borderFrame.grid(row = 2, column = 0, columnspan = 10, sticky = "W")

    bottom_bar = tkinter.Frame(window, relief = "flat", bg = "#333333", pady = 3)
    bottom_bar.grid(row = 3, column = 0, columnspan = 5, rowspan = 1, sticky = "W")

    bold = tkinter.Button(bottom_bar, image = boldButtonImage, bd = 0, bg = "#333333", command = bolder, pady = 4, activebackground = "#333333", fg = "white", padx = 3)
    bold.image = boldButtonImage
    bold.grid(row = 0, column = 1, padx = 5, sticky = "W", pady = 5)

    italic = tkinter.Button(bottom_bar, image = italicButtonImage, bd = 0, bg = "#333333", command = italicizer, pady = 4, activebackground = "#333333", fg = "white", padx = 3)
    italic.image = italicButtonImage
    italic.grid(row = 0, column = 2, padx = 5, sticky = "W", pady = 5)

    underline = tkinter.Button(bottom_bar, image = underButtonImage, bd = 0, bg = "#333333", command = underliner, pady = 4, activebackground = "#333333", fg = "white", padx = 3)
    underline.image = underButtonImage
    underline.grid(row = 0, column = 3, padx = 5, sticky = "W", pady = 5)

    strikeThrough = tkinter.Button(bottom_bar, image = strikeButtonImage, bd = 0, bg = "#333333", pady = 4, command = strikethrough, activebackground = "#333333", fg = "white", padx = 3)
    strikeThrough.image = strikeButtonImage
    strikeThrough.grid(row = 0, column = 4, padx = 5, sticky = "W", pady = 5)

    bullet = tkinter.Button(bottom_bar, image = bulletButtonImage, bd = 0, bg = "#333333", pady = 4, command = bulletList, activebackground = "#333333", fg = "white", padx = 3)
    bullet.image = bulletButtonImage
    bullet.grid(row = 0, column = 5, padx = 5, sticky = "W", pady = 5)

    code = tkinter.Button(bottom_bar, image = codeButtonImage, bd = 0, bg = "#333333", pady = 4, command = codify, activebackground = "#333333", fg = "white", padx = 3)
    code.image = codeButtonImage
    code.grid(row = 0, column = 6, padx = 5, sticky = "W", pady = 5)

    insertl = tkinter.Button(bottom_bar, image = insertlButtonImage, bd = 0, bg = "#333333", pady = 4, command = link, activebackground = "#333333", fg = "white", padx = 3)
    insertl.image = insertlButtonImage
    insertl.grid(row = 0, column = 7, padx = 5, sticky = "W", pady = 5)

    colorText = tkinter.Button(bottom_bar, image = colorButtonImage, bd = 0, bg = "#333333", pady = 4, command = setColor, activebackground = "#333333", fg = "white", padx = 3)
    colorText.image = colorButtonImage
    colorText.grid(row = 0, column = 8, padx = 5, sticky = "W", pady = 5)

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
            window.geometry("310x310" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
            
        startx = event.x_root
        starty = event.y_root

        title_bar.bind('<B1-Motion>', move_window)

    # Keyboard Shortcuts
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

    # Hover Effects
    bold.bind('<Enter>', hoverImageBold)
    bold.bind('<Leave>', NormalImageBold)
    italic.bind('<Enter>', hoverImageItalic)
    italic.bind('<Leave>', NormalImageItalic)
    underline.bind('<Enter>', hoverImageUnder)
    underline.bind('<Leave>', NormalImageUnder)
    strikeThrough.bind('<Enter>', hoverImageStrike)
    strikeThrough.bind('<Leave>', NormalImageStrike)
    bullet.bind('<Enter>', hoverImageBullet)
    bullet.bind('<Leave>', NormalImageBullet)
    code.bind('<Enter>', hoverImageCode)
    code.bind('<Leave>', NormalImageCode)
    new.bind('<Enter>', hoverImageNew)
    new.bind('<Leave>', NormalImageNew)
    save.bind('<Enter>', hoverImageSave)
    save.bind('<Leave>', NormalImageSave)
    openlink.bind('<Enter>', hoverImageOpen)
    openlink.bind('<Leave>', NormalImageOpen)
    menu.bind('<Enter>', hoverImageMenu)
    menu.bind('<Leave>', NormalImageMenu)
    close_button.bind('<Enter>', hoverImageClose)
    close_button.bind('<Leave>', NormalImageClose)
    insertl.bind('<Enter>', hoverImageLink)
    insertl.bind('<Leave>', NormalImageLink)
    colorText.bind('<Enter>', hoverImageTsize)
    colorText.bind('<Leave>', NormalImageTsize)

    # Desktop Gadget and Autosave
    window.after(10, topOrNot)
    window.after(3000, autoSave)
    
    # Update the window
    window.mainloop()

mainWindow()