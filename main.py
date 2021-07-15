import tkinter
import tkinter.messagebox
import pygetwindow as gw
import os
import webbrowser
import re
import glob
import argparse
import tkinter.ttk
import subprocess
from tkinter import font
from random import randint
from tkinter import filedialog
from tkinter import PhotoImage
from string import ascii_uppercase
from PIL import Image
from datetime import datetime


# Argument Parser
parser = argparse.ArgumentParser(description="Open a file")
parser.add_argument(
    "file",
    default=None,
    nargs="?",
    help="Name of the file to load")

args = parser.parse_args()

# Defining Window Properties
root = tkinter.Tk()
root.withdraw()

window = tkinter.Toplevel()
window.title("Notes window")
window.attributes("-toolwindow", True)
window.overrideredirect(1)
window.geometry("310x310+" + str(randint(10, 900)) +
                "+" + str(randint(10, 500)))
window.config(bg="#333333")
window.wait_visibility(window)

# Configuring grid
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=100000)
window.grid_columnconfigure(3, weight=1000)
window.grid_columnconfigure(4, weight=0)
window.grid_columnconfigure(5, weight=0)
window.grid_columnconfigure(6, weight=0)

openedFileName = False  # Getting opened file name

saved = False  # The saved variable

images = []  # The list with all images, index, and name

# Default values of the themes
global pinkTheme
global yellowTheme
global greenTheme
global blueTheme
pinkTheme = False
yellowTheme = True
greenTheme = False
blueTheme = False

# Getting images (normal) for the buttons:
newButtonImage = PhotoImage(file="res/images/iconset/new.png")
saveButtonImage = PhotoImage(file="res/images/iconset/save.png")
linkButtonImage = PhotoImage(file="res/images/iconset/open.png")
menuButtonImage = PhotoImage(file="res/images/iconset/menu.png")
closeButtonImage = PhotoImage(file="res/images/iconset/close.png")
boldButtonImage = PhotoImage(file="res/images/iconset/bold.png")
italicButtonImage = PhotoImage(file="res/images/iconset/italic.png")
underButtonImage = PhotoImage(file="res/images/iconset/underline.png")
strikeButtonImage = PhotoImage(file="res/images/iconset/strikethrough.png")
bulletButtonImage = PhotoImage(file="res/images/iconset/bullet.png")
codeButtonImage = PhotoImage(file="res/images/iconset/code.png")
insertlButtonImage = PhotoImage(file="res/images/iconset/link.png")
colorButtonImage = PhotoImage(file="res/images/iconset/color.png")
photoButtonImage = PhotoImage(file="res/images/iconset/photo.png")


# Getting images (hover) for the buttons:
newButtonImageAfter = PhotoImage(file="res/images/iconset/new1.png")
saveButtonImageAfter = PhotoImage(file="res/images/iconset/save1.png")
linkButtonImageAfter = PhotoImage(file="res/images/iconset/open1.png")
menuButtonImageAfter = PhotoImage(file="res/images/iconset/menu1.png")
closeButtonImageAfter = PhotoImage(file="res/images/iconset/close1.png")
boldButtonImageAfter = PhotoImage(file="res/images/iconset/bold1.png")
italicButtonImageAfter = PhotoImage(file="res/images/iconset/italic1.png")
underButtonImageAfter = PhotoImage(file="res/images/iconset/underline1.png")
strikeButtonImageAfter = PhotoImage(
    file="res/images/iconset/strikethrough1.png")
bulletButtonImageAfter = PhotoImage(file="res/images/iconset/bullet1.png")
codeButtonImageAfter = PhotoImage(file="res/images/iconset/code1.png")
insertlButtonImageAfter = PhotoImage(file="res/images/iconset/link1.png")
colorButtonImageAfter = PhotoImage(file="res/images/iconset/color1.png")
photoButtonImageAfter = PhotoImage(file="res/images/iconset/photo1.png")

allImagesGroup = []  # Reference list with images in it
imgNumberName = 0  # A variable used to name images in chronological order

accentItems = []  # List that holds all items that have accent color

deletedImages = []  # List that holds all images that need to be deleted


def fetchDrivePath() -> str:
    """The drive in which the script is running"""

    for drive in ascii_uppercase:
        if os.path.exists(f"{drive}:\\Users"):
            return drive + ":\\"
    return ""


def createNewWindow(_=False):
    """Creating a new window"""

    # Check whether the exe or the python script is being used
    try:
        exePath = f"{os.path.dirname(os.path.realpath(__file__))}" \
            "\\Textylic.exe"
        subprocess.check_call(
            exePath,
            shell=True)
        subprocess.Popen(
            exePath,
            shell=True)
    except subprocess.CalledProcessError:
        subprocess.Popen(
            f"python {os.path.dirname(os.path.realpath(__file__))}\\main.py",
            shell=True)


def openNotesList():
    """Opening the folder in which all the notes are stored"""

    subprocess.Popen(
        f"explorer {os.path.dirname(os.path.realpath(__file__))}\\Notes",
        shell=True)


def bolder(_=False):
    """Bold button function"""

    bold_font = font.Font(notes, notes.cget("font"))
    bold_font.configure(weight="bold")

    italicBold_font = font.Font(notes, notes.cget("font"))
    italicBold_font.configure(slant="italic", weight="bold")

    underBold_font = font.Font(notes, notes.cget("font"))
    underBold_font.configure(underline=True, weight="bold")

    strikeBold_font = font.Font(notes, notes.cget("font"))
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


def italicizer(_=False):
    """Italic button function"""

    italic_font = font.Font(notes, notes.cget("font"))
    italic_font.configure(slant="italic")

    boldItalic_font = font.Font(notes, notes.cget("font"))
    boldItalic_font.configure(slant="italic", weight="bold")

    underItalic_font = font.Font(notes, notes.cget("font"))
    underItalic_font.configure(underline=True, slant="italic")

    strikeItalic_font = font.Font(notes, notes.cget("font"))
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


def codify(_=False):
    """Code button function"""

    notes.tag_configure("code", font="Consolas 11")
    current_tags = notes.tag_names("sel.first")

    if "code" in current_tags:
        notes.tag_remove("code", "sel.first", "sel.last")
    else:
        notes.tag_add("code", "sel.first", "sel.last")
    return "break"


def underliner(_=False):
    """Underline button function"""

    under_font = font.Font(notes, notes.cget("font"))
    under_font.configure(underline=True)

    boldUnder_font = font.Font(notes, notes.cget("font"))
    boldUnder_font.configure(underline=True, weight="bold")

    italicUnder_font = font.Font(notes, notes.cget("font"))
    italicUnder_font.configure(underline=True, slant="italic")

    strikeUnder_font = font.Font(notes, notes.cget("font"))
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


def strikethrough(_=False):
    """Strikethrough button function"""

    strike_font = font.Font(notes, notes.cget("font"))
    strike_font.configure(overstrike=True)

    boldStrike_font = font.Font(notes, notes.cget("font"))
    boldStrike_font.configure(overstrike=True, weight="bold")

    italicStrike_font = font.Font(notes, notes.cget("font"))
    italicStrike_font.configure(overstrike=True, slant="italic")

    underStrike_font = font.Font(notes, notes.cget("font"))
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
    """Bulleted list button function"""

    selection = notes.selection_get()
    current_tags = notes.tag_names("sel.first")

    if "\n" not in selection:
        if "bullet" not in current_tags:
            index_1 = float(notes.index("sel.first"))
            index_2 = float(notes.index("sel.last"))
            bulleted_str = "\t•  " + str(selection)
            notes.delete(index_1, index_2)
            notes.insert(index_1, bulleted_str)
            lenBulletString = len(bulleted_str)
            lenBulletString = notes.index(index_1 + lenBulletString)
            notes.tag_add("bullet", index_1, lenBulletString)
        elif "bullet" in current_tags:
            index_1 = float(notes.index("sel.first"))
            index_2 = float(notes.index("sel.last"))
            selected = notes.selection_get()
            selected = str(selected)
            selected = selected.replace("\t•  ", "")
            notes.insert("sel.first", selected)
            notes.delete("sel.first", "sel.last")
            lenBulletString = len(selected)
            lenBulletString = notes.index(lenBulletString)
            notes.tag_remove("bullet", index_1, lenBulletString)
    elif "\n" in selection:
        if "bullet" not in current_tags:
            index_1 = float(notes.index("sel.first"))
            index_2 = float(notes.index("sel.last"))
            select = notes.selection_get()
            bulleted_str = select.replace("\n", "\n\t•  ")
            bulleted_str = "\t•  " + str(bulleted_str)
            notes.delete(str(index_1), str(index_2))
            notes.insert(index_1, bulleted_str)
            lenBulletString = len(bulleted_str)
            lenBulletString = notes.index(index_1 + lenBulletString)
            notes.tag_add("bullet", index_1, lenBulletString)
        elif "bullet" in current_tags:
            index_1 = float(notes.index("sel.first"))
            index_2 = float(notes.index("sel.last"))
            selected = selection.replace("\n\t•  ", "\n")
            selected = selected.replace("\t•  ", "")
            notes.insert("sel.first", selected)
            notes.delete("sel.first", "sel.last")
            lenBulletString = len(selected)
            lenBulletString = notes.index(lenBulletString)
            notes.tag_remove("bullet", index_1, lenBulletString)
    return "break"


def link(_=False):
    """Link button function"""

    under_font = font.Font(notes, notes.cget("font"))
    under_font.configure(underline=True)

    notes.tag_configure("link", font=under_font, foreground="#00AFEC")
    current_tags = notes.tag_names("sel.first")

    if "link" in current_tags:
        notes.tag_remove("link", "sel.first", "sel.last")
    else:
        notes.tag_add("link", "sel.first", "sel.last")
    return "break"


def setColor():
    """Change Text Color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    if yellowTheme is True:
        notes.tag_configure("emphColor", foreground="#E6B905")
    elif pinkTheme is True:
        notes.tag_configure("emphColor", foreground="#EB8EC6")
    elif greenTheme is True:
        notes.tag_configure("emphColor", foreground="#65BA5A")
    elif blueTheme is True:
        notes.tag_configure("emphColor", foreground="#59C0E7")
    current_tags = notes.tag_names("sel.first")

    if "emphColor" in current_tags:
        notes.tag_remove("emphColor", "sel.first", "sel.last")
    else:
        notes.tag_add("emphColor", "sel.first", "sel.last")

    return "break"


def openLink(_=False):
    """Open link button function"""

    current_tags = notes.tag_names("sel.first")
    if "link" in current_tags:
        url = notes.selection_get()
        webbrowser.open_new(url)
    return "break"


def openReadme(_=False):
    """Open the README.md on GitHub and the Textylic website"""

    webbrowser.open_new(
        "https://github.com/akhilesh-balaji/Textylic/blob/master/README.md")
    webbrowser.open_new("https://akhilesh-balaji.github.io/Textylic/")
    return "break"


def hoverImageBold(_=False):
    """Changing the image of bold button on hover"""

    bold.configure(image=boldButtonImageAfter)


def NormalImageBold(_=False):
    """Getting the normal image for the bold button function"""

    bold.configure(image=boldButtonImage)


def hoverImageItalic(_=False):
    """Changing the image of italic button on hover"""

    italic.configure(image=italicButtonImageAfter)


def NormalImageItalic(_=False):
    """Getting the normal image for the italic button function"""

    italic.configure(image=italicButtonImage)


def hoverImageUnder(_=False):
    """Changing the image of underline button on hover"""

    underline.configure(image=underButtonImageAfter)


def NormalImageUnder(_=False):
    """Getting the normal image for the underline button function"""

    underline.configure(image=underButtonImage)


def hoverImageStrike(_=False):
    """Changing the image of strikethrough button on hover"""

    strikeThrough.configure(image=strikeButtonImageAfter)


def NormalImageStrike(_=False):
    """Getting the normal image for the strikethrough button function"""

    strikeThrough.configure(image=strikeButtonImage)


def hoverImageBullet(_=False):
    """Changing the image of bulleted list button on hover"""

    bullet.configure(image=bulletButtonImageAfter)


def NormalImageBullet(_=False):
    """Getting the normal image for the bulleted list button function"""

    bullet.configure(image=bulletButtonImage)


def hoverImageCode(_=False):
    """Changing the image of code-ify button on hover"""

    code.configure(image=codeButtonImageAfter)


def NormalImageCode(_=False):
    """Getting the normal image for the code-ify button function"""

    code.configure(image=codeButtonImage)


def hoverImageNew(_=False):
    """Changing the image of new button on hover"""

    new.configure(image=newButtonImageAfter)


def NormalImageNew(_=False):
    """Getting the normal image for the new button function"""

    new.configure(image=newButtonImage)


def hoverImageSave(_=False):
    """Changing the image of save button on hover"""

    save.configure(image=saveButtonImageAfter)


def NormalImageSave(_=False):
    """Getting the normal image for the save button function"""

    save.configure(image=saveButtonImage)


def hoverImageOpen(_=False):
    """Changing the image of open note button on hover"""

    openlink.configure(image=linkButtonImageAfter)


def NormalImageOpen(_=False):
    """Getting the normal image for the open note button function"""

    openlink.configure(image=linkButtonImage)


def hoverImageMenu(_=False):
    """Changing the image of menu button on hover"""

    menu.configure(image=menuButtonImageAfter)


def NormalImageMenu(_=False):
    """Getting the normal image for the menu button function"""

    menu.configure(image=menuButtonImage)


def hoverImageClose(_=False):
    """Changing the image of close button on hover"""

    close_button.configure(image=closeButtonImageAfter)


def NormalImageClose(_=False):
    """Getting the normal image for the close button function"""

    close_button.configure(image=closeButtonImage)


def hoverImageLink(_=False):
    """Changing the image of hyperlink button on hover"""

    insertl.configure(image=insertlButtonImageAfter)


def NormalImageLink(_=False):
    """Getting the normal image for the hyperlink button function"""

    insertl.configure(image=insertlButtonImage)


def hoverImageTsize(_=False):
    """Changing the image of color button on hover"""

    colorText.configure(image=colorButtonImageAfter)


def NormalImageTsize(_=False):
    """Getting the normal image for the color button function"""

    colorText.configure(image=colorButtonImage)


def hoverImagePhoto(_=False):
    """Changing the image of image button on hover"""

    photoInsert.configure(image=photoButtonImageAfter)


def NormalImagePhoto(_=False):
    """Getting the normal image for the image button function"""

    photoInsert.configure(image=photoButtonImage)


def getTags(start, end) -> list:
    """
    Get the tags (bold, italic, etc.) and their indices in the Text widget.

    It gets the tags for each character till the end, and stores the end index
    when the tag changes.
    """

    index = start
    tagname = []
    starttagindex = index
    prevtag = notes.tag_names(index)

    try:
        tagname.append([starttagindex, "end", notes.tag_names(index)])
    except BaseException:
        tagname.append([starttagindex, "end", ("",)])

    while notes.compare(index, "<", end):
        if notes.tag_names(index) != prevtag:
            # If the tag name at the current index is not equal to the
            # previous index's tag name...
            if len(notes.tag_names(index)) <= 0:
                # If the legnth of the tuple containing the tag names at the
                # current index is less that or equal to 0, it means that
                # there are no tags here.
                starttagindex = index
                legnth = len(tagname)
                tagname[legnth - 1][1] = index
                tagname.append([starttagindex, "end", ("",)])
            else:
                # Otherwise, it means that there are tags here.
                starttagindex = index
                legnth = len(tagname)
                tagname[legnth - 1][1] = index
                tagname.append([starttagindex, "end", notes.tag_names(index)])

        prevtag = notes.tag_names(index)
        index = notes.index(f"{index}+1c")

    return tagname


def photoInserter():
    """'Insert photo' button function"""

    global allImagesGroup
    global saved
    global images
    global imgNumberName
    global dateTimeNow
    global openedFileName

    dateTimeNow = str(datetime.now())
    dateTimeNow = dateTimeNow.replace("-", "_")
    dateTimeNow = dateTimeNow.replace(" ", "_")
    dateTimeNow = dateTimeNow.replace(":", "")
    dateTimeNow = dateTimeNow.replace(".", "")

    imgNumberName = imgNumberName + 1

    photo = filedialog.askopenfilename(
        initialdir="~/Pictures",
        title="Choose an Image:",
        filetypes=(
            ("PNG",
             "*.png"),
            ("JPG",
             "*.jpg"),
            ("JPEG",
             "*.jpeg"),
        ))
    imgFile = Image.open(photo)
    imgFile.thumbnail((280, 280))
    imgFile.save(f"./res/cache_images_/{dateTimeNow}.png")

    imgToInsert = PhotoImage(file=f"./res/cache_images_/{dateTimeNow}.png")
    allImagesGroup.append(imgToInsert)
    images.append(
        [f"./res/cache_images_/{dateTimeNow}",
            notes.index("insert"),
            f"image{imgNumberName}"])
    notes.image_create(
        "insert",
        image=imgToInsert,
        name=f"image{imgNumberName}")
    imgFile.close()
    photo.close()


def openFile(file: str):
    """Open a file with the file dialog"""

    global saved
    global images
    global allImagesGroup

    noteFile = file
    if noteFile:
        global openedFileName
        openedFileName = noteFile
    noteFile = open(noteFile, "r")
    read = noteFile.read()

    matchStyle = re.match(
        r".*<style>\n(.*)\n</style>",
        str(read),
        flags=re.DOTALL | re.MULTILINE)
    matchImg = re.match(
        r".*<images>\n(.*)\n</images>",
        str(read),
        flags=re.DOTALL | re.MULTILINE)
    matchTheme = re.match(
        r".*<colortheme>\n(.*)\n</colortheme>",
        str(read),
        flags=re.DOTALL | re.MULTILINE)

    read = re.sub("<style>.*$", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("<content>\n", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("\n*</content>\n\n", "", read,
                  flags=re.DOTALL | re.MULTILINE)

    notes.delete("1.0", "end")
    notes.insert("end", read)

    if matchStyle:
        # Bold fonts and tags
        formatting = matchStyle.group(1)
        formatting = eval(formatting)

        bold_font = font.Font(notes, notes.cget("font"))
        bold_font.configure(weight="bold")

        italicBold_font = font.Font(notes, notes.cget("font"))
        italicBold_font.configure(slant="italic", weight="bold")

        underBold_font = font.Font(notes, notes.cget("font"))
        underBold_font.configure(underline=True, weight="bold")

        strikeBold_font = font.Font(notes, notes.cget("font"))
        strikeBold_font.configure(overstrike=True, weight="bold")

        notes.tag_configure("bold", font=bold_font)
        notes.tag_configure("italicBold", font=italicBold_font)
        notes.tag_configure("underBold", font=underBold_font)
        notes.tag_configure("strikeBold", font=strikeBold_font)

        # Italic fonts and tags
        italic_font = font.Font(notes, notes.cget("font"))
        italic_font.configure(slant="italic")

        boldItalic_font = font.Font(notes, notes.cget("font"))
        boldItalic_font.configure(slant="italic", weight="bold")

        underItalic_font = font.Font(notes, notes.cget("font"))
        underItalic_font.configure(underline=True, slant="italic")

        strikeItalic_font = font.Font(notes, notes.cget("font"))
        strikeItalic_font.configure(overstrike=True, slant="italic")

        notes.tag_configure("italic", font=italic_font)
        notes.tag_configure("boldItalic", font=boldItalic_font)
        notes.tag_configure("underItalic", font=underItalic_font)
        notes.tag_configure("strikeItalic", font=strikeItalic_font)

        # Code font and tags
        notes.tag_configure("code", font="Consolas 11")

        # Underline font and tags
        under_font = font.Font(notes, notes.cget("font"))
        under_font.configure(underline=True)

        boldUnder_font = font.Font(notes, notes.cget("font"))
        boldUnder_font.configure(underline=True, weight="bold")

        italicUnder_font = font.Font(notes, notes.cget("font"))
        italicUnder_font.configure(underline=True, slant="italic")

        strikeUnder_font = font.Font(notes, notes.cget("font"))
        strikeUnder_font.configure(overstrike=True, underline=True)

        notes.tag_configure("underline", font=under_font)
        notes.tag_configure("boldUnder", font=boldUnder_font)
        notes.tag_configure("italicUnder", font=italicUnder_font)
        notes.tag_configure("strikeUnder", font=strikeUnder_font)

        # Link font
        notes.tag_configure("link", font=under_font, foreground="#00AFEC")

        # Text color
        global pinkTheme
        global yellowTheme
        global greenTheme
        global blueTheme
        if yellowTheme is True:
            notes.tag_configure("emphColor", foreground="#E6B905")
        elif pinkTheme is True:
            notes.tag_configure("emphColor", foreground="#EB8EC6")
        elif greenTheme is True:
            notes.tag_configure("emphColor", foreground="#65BA5A")
        elif blueTheme is True:
            notes.tag_configure("emphColor", foreground="#59C0E7")

        for format in formatting:
            # Apply formatting
            for tag in format[2]:
                notes.tag_add(str(tag).strip("}{/.\\"), format[0], format[1])

    if matchImg:
        # Getting the list of images
        images = eval(matchImg.group(1))
        allImagesGroup = []
        for imageList in images:
            # Insert the images at appropriate index
            imageToInsert = PhotoImage(file=f"{imageList[0]}.png")
            notes.insert(f"{imageList[1]}-1c", "\n")
            notes.image_create(
                imageList[1],
                image=imageToInsert,
                name=imageList[2])
            allImagesGroup.append(imageToInsert)

    if matchTheme:
        # Getting the theme of the note
        exec(matchTheme.group(1))

    noteFile.close()
    saved = True
    # Messagebox
    openedFileNameStrip = re.sub("C:/.*/", "", str(openedFileName))
    tkinter.messagebox.showinfo(
        " ", f"Successfully opened note \"{openedFileNameStrip}\"   ")
    return "break"


def openFileChoose(_=False):
    """Open a file with the file dialog"""

    openFile((filedialog.askopenfilename(initialdir="./Notes",
                                         title="Choose a note:", filetypes=(
                                             ("Textylic file", "*.txtlyc"),))))
    return "break"


def saveNoteAs(_=False):
    """Save the note as a file name"""

    noteFile = filedialog.asksaveasfilename(
        confirmoverwrite=True,
        defaultextension=".txtlyc",
        filetypes=(
            ("Textylic file", "*.txtlyc"),),
        initialdir="./Notes",
        title="Save your note:")
    if noteFile:
        global saved
        saved = True
        global openedFileName
        openedFileName = noteFile
        noteFile = open(noteFile, "w")
        noteFile.write(notes.get(1.0, "end"))
        noteFile.close()
        # Messagebox
        openedFileNameStrip = re.sub("C:/.*/", "", str(openedFileName))
        tkinter.messagebox.showinfo(
            " ", f"Successfully saved note as \"{openedFileNameStrip}\"   ")
    return "break"


def saveNote(_=False):
    """Save the note"""

    global saved
    global openedFileName
    global images
    global deletedImages
    global allImagesGroup
    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme

    for imgName in notes.image_names():
        # Saving the list of image names
        index = notes.index(str(imgName))

        for image in images:
            # Deleting unused images from the list
            if image[2] in notes.image_names():
                if image[2] == imgName:
                    image[1] = index
            else:
                deletedImages.append(image)

    for deletedImage in deletedImages:
        # Deleting the unused images from `images` list
        try:
            images.remove(deletedImage)
        except BaseException:
            pass

    if openedFileName:
        # If a file is not being saved the first time, append additional data
        # to it
        noteFile = open(openedFileName, "w")
        noteFile.write(
            "<content>\n{}\n</content>\n\n".format(notes.get(1.0, "end")))
        noteFile.write(
            "<style>\n{}\n</style>\n\n".format(getTags("1.0", "end")))
        noteFile.write("<images>\n{}\n</images>\n\n".format(images))

        if blueTheme is True:
            noteFile.write("<colortheme>\naccentblue()\n</colortheme>")
        elif pinkTheme is True:
            noteFile.write("<colortheme>\naccentpink()\n</colortheme>")
        elif yellowTheme is True:
            noteFile.write("<colortheme>\naccentyellow()\n</colortheme>")
        elif greenTheme is True:
            noteFile.write("<colortheme>\naccentgreen()\n</colortheme>")

        noteFile.close()
        saved = True
        getTags("1.0", "end")
    else:
        saveNoteAs()
    return "break"


def clearCache():
    """Clearing the unused images from the `cache_images_` folder"""

    imagesToBeSaved = []
    pathToNotes = "./Notes"
    pathToNotes = os.path.join(pathToNotes, '*.txtlyc')
    pathToNotes = pathToNotes.replace("\\", "/")

    pathToImages = "./res/cache_images_"
    pathToImages = os.path.join(pathToImages, '*.*')
    pathToImages = pathToImages.replace("\\", "/")

    for filename in glob.glob(pathToNotes):
        # For all the images in the `cache_images_` folder check if they are
        # in the `images` list for every note
        formattedFileName = filename.replace("\\", "/")
        noteFile = open(f"{formattedFileName}", "r")
        readContent = noteFile.read()
        matchImg = re.match(
            r".*<images>\n(.*)\n</images>",
            str(readContent),
            flags=re.DOTALL | re.MULTILINE)

        if matchImg:
            images = eval(matchImg.group(1))
            for image in images:
                imagesToBeSaved.append(f"{image[0]}.png")

        noteFile.close()

    for imageFile in glob.glob(pathToImages):
        # Deleting the unused images
        imagesToBeSavedSet = set(imagesToBeSaved)
        formattedImgFileName = imageFile.replace("\\", "/")
        if formattedImgFileName not in imagesToBeSavedSet:
            os.remove(formattedImgFileName)


def autoSave():
    """Auto saves the note"""

    global saved
    if saved is True:
        saveNote()
    window.after(3000, autoSave)


def windowdestroy(_=False):
    """Close the window"""

    global openedFileName

    def whitespaceStr(strg, search=re.compile(r"[^\s]+").search):
        return not bool(search(strg))

    if (not openedFileName) and (not whitespaceStr(notes.get("1.0", "end"))):
        # Confirmbox
        confirmSave = tkinter.messagebox.askyesnocancel("Confirmation",
                                                        "Do you want to save this note \
                                            before you leave?   ",
                                                        icon="warning",
                                                        default="no")
        if confirmSave is True:
            saveNoteAs()
        elif confirmSave is False:
            root.destroy()
        else:
            pass
    else:
        root.destroy()


def accentpink():
    """Pink accent color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    pinkTheme = True
    yellowTheme = False
    greenTheme = False
    blueTheme = False
    for item in accentItems:
        item.configure(bg="#EB8EC6", activebackground="#EB8EC6")
    titleBar.configure(bg="#EB8EC6")
    menu.configure(activebackground="#EB8EC6")
    notes.tag_configure("emphColor", foreground="#EB8EC6")
    window.update()


def accentyellow():
    """Yellow accent color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    pinkTheme = False
    yellowTheme = True
    greenTheme = False
    blueTheme = False
    for item in accentItems:
        item.configure(bg="#E6B905", activebackground="#E6B905")
    titleBar.configure(bg="#E6B905")
    notes.tag_configure("emphColor", foreground="#E6B905")
    menu.configure(activebackground="#E6B905")
    window.update()


def accentgreen():
    """Green accent color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    pinkTheme = False
    yellowTheme = False
    greenTheme = True
    blueTheme = False
    for item in accentItems:
        item.configure(bg="#65BA5A", activebackground="#65BA5A")
    titleBar.configure(bg="#65BA5A")
    notes.tag_configure("emphColor", foreground="#65BA5A")
    menu.configure(activebackground="#65BA5A")
    window.update()


def accentblue():
    """Blue accent color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    pinkTheme = False
    yellowTheme = False
    greenTheme = False
    blueTheme = True
    for item in accentItems:
        item.configure(bg="#59C0E7", activebackground="#59C0E7")
    titleBar.configure(bg="#59C0E7")
    notes.tag_configure("emphColor", foreground="#59C0E7")
    menu.configure(activebackground="#59C0E7")
    window.update()


def topOrNot():
    """
    Detects wheather the window should be shown or not.

    Makes it act like a Desktop widget.
    """

    # TODO: Refine this logic
    # HELP WANTED

    windows = gw.getActiveWindow()

    # Desktop Widget logic
    if windows is None:
        window.deiconify()
        window.lift()
        window.attributes("-topmost", True)
    else:
        if windows.isMaximized:
            window.lower()
            window.attributes("-topmost", False)
        elif (not windows.isMaximized and windows.title != "" and
                windows.title != "Notes window" and windows.title !=
                "Choose a note:" and windows.title != "Save your note:" and
                windows.title != "Choose an Image:" and windows.title != "tk"):
            window.deiconify()
            window.attributes("-topmost", False)
            window.lower()
        elif (not windows.isMaximized and windows.title != "" and
                windows.title == "Notes window" or windows.title ==
                "Choose a note:" or windows.title == "Save your note:" or
                windows.title == "Choose an Image:"):
            window.attributes("-topmost", False)
        elif windows.title == "tk":
            window.deiconify()
            window.lift()
            window.attributes("-topmost", True)
        else:
            window.deiconify()
            window.lift()
            window.attributes("-topmost", True)

    window.after(10, topOrNot)


def getPos(event):
    """Get the position of the window"""

    xwin = window.winfo_x()
    ywin = window.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx

    def moveWindow(event):
        """Moving the window on mouse move"""

        window.geometry(
            "310x310" + f'+{event.x_root + xwin}+{event.y_root + ywin}')

    startx = event.x_root
    starty = event.y_root

    titleBar.bind('<B1-Motion>', moveWindow)


winDrive = fetchDrivePath()  # The windows directory letter

# Defining Title Bar Elements
titleBar = tkinter.Frame(window, relief="flat", bg="#E6B905")

new = tkinter.Button(
    titleBar,
    image=newButtonImage,
    bd=0,
    bg="#E6B905",
    command=createNewWindow,
    activebackground="#E6B905")
new.image = newButtonImage
new.grid(row=0, column=0, padx=5, sticky="W", pady=5)
new.image = newButtonImage
accentItems.append(new)

# Save
save = tkinter.Button(
    titleBar,
    image=saveButtonImage,
    bd=0,
    bg="#E6B905",
    pady=4,
    activebackground="#E6B905",
    command=saveNote)
save.image = saveButtonImage
save.grid(row=0, column=1, padx=5, sticky="W", pady=5)
accentItems.append(save)

# Link opening button
openlink = tkinter.Button(
    titleBar,
    image=linkButtonImage,
    bd=0,
    bg="#E6B905",
    pady=4,
    command=openLink,
    activebackground="#E6B905")
openLink.image = linkButtonImage
openlink.grid(row=0, column=2, padx=5, sticky="W", pady=5)
accentItems.append(openlink)

# Notes Text widget container
notesFrame = tkinter.Frame(
    window,
    relief="flat",
    bg="#333333",
    height=200,
    width=297)
notesFrame.grid(row=1, column=0, columnspan=5)

# Main Text input
notes = tkinter.Text(
    notesFrame,
    undo=True,
    font="Segoe_UI 11",
    bg="#333333",
    padx=5,
    pady=10,
    bd=0,
    fg="white",
    insertbackground="white",
    relief="flat",
    selectbackground="#616161",
    wrap="word",
    height=10.5,
    width=36,
    tabs=(
        "0.5c",
        "3c",
         "5c"))
notes.grid(row=0, column=0, rowspan=5, columnspan=5)
notes.delete("1.0", "end")
segoe_font = font.Font(notes, notes.cget("font"))
segoe_font.configure(family="Segoe UI", size=11)
notes.configure(font=segoe_font)

# Extra Menu
menu = tkinter.Menubutton(
    titleBar,
    image=menuButtonImage,
    bd=0,
    bg="#E6B905",
    relief="flat",
    pady=4,
    activebackground="#E6B905")
menu.image = menuButtonImage
menu.grid(row=0, column=3, padx=5, sticky="W", pady=5)
accentItems.append(menu)

segoe_font_menu = font.Font()
segoe_font_menu.configure(family="Segoe UI", size=10)

menu.menu = tkinter.Menu(
    menu,
    tearoff=0,
    bd=0,
    relief="solid",
    font=segoe_font_menu,
    activeborderwidth=0,
    activebackground="#c4c4c4",
    activeforeground="#000000",
    selectcolor="black")

advancedMenu = tkinter.Menu(
    menu.menu,
    tearoff=0,
    bd=0,
    relief="solid",
    font=segoe_font_menu,
    activeborderwidth=0,
    activebackground="#c4c4c4",
    activeforeground="#000000",
    selectcolor="black")
advancedMenu.add_command(label="Notes List", command=openNotesList)
advancedMenu.add_command(label="Clear Cache", command=clearCache)
# advancedMenu.add_command(label="Minimize to systray", command=minSysTray)

menu["menu"] = menu.menu

menu.menu.add_command(label="Choose theme:")
menu.menu.add_radiobutton(label="Blue", command=accentblue)
menu.menu.add_radiobutton(label="Yellow", command=accentyellow)
menu.menu.add_radiobutton(label="Green", command=accentgreen)
menu.menu.add_radiobutton(label="Pink", command=accentpink)

menu.menu.add_separator()

menu.menu.add_command(label="Open Note", command=openFileChoose)
menu.menu.add_command(
    label="Save Note",
    command=saveNote,
    accelerator="(Ctr+s)")
menu.menu.add_cascade(label="More...", menu=advancedMenu)
menu.menu.add_separator()
menu.menu.add_command(
    label="Undo",
    command=notes.edit_undo,
    accelerator="(Ctr+z)")
menu.menu.add_command(
    label="Redo",
    command=notes.edit_redo,
    accelerator="(Ctr+y)")
menu.menu.add_command(
    label="Quit",
    command=windowdestroy,
    accelerator="(Ctr+q)")
menu.menu.add_command(label="Help/About", command=openReadme)

close_button = tkinter.Button(
    titleBar,
    image=closeButtonImage,
    bd=0,
    bg="#E6B905",
    command=windowdestroy,
    pady=4,
    activebackground="#E6B905")
close_button.image = closeButtonImage
close_button.grid(row=0, column=6, padx=150, sticky="E")
accentItems.append(close_button)

# Bottom formatting bar
borderFrame = tkinter.Frame(window, height=0.5, width=2000000, pady=10)
borderFrame.grid(row=2, column=0, columnspan=10, sticky="W")

bottom_bar = tkinter.Frame(window, relief="flat", bg="#333333", pady=3)
bottom_bar.grid(row=3, column=0, columnspan=5, rowspan=1, sticky="W")

bold = tkinter.Button(
    bottom_bar,
    image=boldButtonImage,
    bd=0,
    bg="#333333",
    command=bolder,
    pady=4,
    activebackground="#333333",
    fg="white",
    padx=3)
bold.image = boldButtonImage
bold.grid(row=0, column=1, padx=5, sticky="W", pady=5)

italic = tkinter.Button(
    bottom_bar,
    image=italicButtonImage,
    bd=0,
    bg="#333333",
    command=italicizer,
    pady=4,
    activebackground="#333333",
    fg="white",
    padx=3)
italic.image = italicButtonImage
italic.grid(row=0, column=2, padx=5, sticky="W", pady=5)

underline = tkinter.Button(
    bottom_bar,
    image=underButtonImage,
    bd=0,
    bg="#333333",
    command=underliner,
    pady=4,
    activebackground="#333333",
    fg="white",
    padx=3)
underline.image = underButtonImage
underline.grid(row=0, column=3, padx=5, sticky="W", pady=5)

strikeThrough = tkinter.Button(
    bottom_bar,
    image=strikeButtonImage,
    bd=0,
    bg="#333333",
    pady=4,
    command=strikethrough,
    activebackground="#333333",
    fg="white",
    padx=3)
strikeThrough.image = strikeButtonImage
strikeThrough.grid(row=0, column=4, padx=5, sticky="W", pady=5)

bullet = tkinter.Button(
    bottom_bar,
    image=bulletButtonImage,
    bd=0,
    bg="#333333",
    pady=4,
    command=bulletList,
    activebackground="#333333",
    fg="white",
    padx=3)
bullet.image = bulletButtonImage
bullet.grid(row=0, column=5, padx=5, sticky="W", pady=5)

code = tkinter.Button(
    bottom_bar,
    image=codeButtonImage,
    bd=0,
    bg="#333333",
    pady=4,
    command=codify,
    activebackground="#333333",
    fg="white",
    padx=3)
code.image = codeButtonImage
code.grid(row=0, column=6, padx=5, sticky="W", pady=5)

insertl = tkinter.Button(
    bottom_bar,
    image=insertlButtonImage,
    bd=0,
    bg="#333333",
    pady=4,
    command=link,
    activebackground="#333333",
    fg="white",
    padx=3)
insertl.image = insertlButtonImage
insertl.grid(row=0, column=7, padx=5, sticky="W", pady=5)

colorText = tkinter.Button(
    bottom_bar,
    image=colorButtonImage,
    bd=0,
    bg="#333333",
    pady=4,
    command=setColor,
    activebackground="#333333",
    fg="white",
    padx=3)
colorText.image = colorButtonImage
colorText.grid(row=0, column=8, padx=5, sticky="W", pady=5)

photoInsert = tkinter.Button(
    bottom_bar,
    image=photoButtonImage,
    bd=0,
    bg="#333333",
    pady=4,
    command=photoInserter,
    activebackground="#333333",
    fg="white",
    padx=3)
photoInsert.image = colorButtonImage
photoInsert.grid(row=0, column=9, padx=5, sticky="W", pady=5)

# Positioning title bar and adding drag function
titleBar.grid(row=0, column=0, columnspan=5, sticky="W")

# Keyboard Shortcuts
titleBar.bind("<Button-1>", getPos)
notes.bind("<Control-Key-b>", bolder)
notes.bind("<Control-Key-i>", italicizer)
notes.bind("<Control-Key-u>", underliner)
notes.bind("<Control-Key-t>", codify)
notes.bind("<Control-Key-q>", windowdestroy)
notes.bind("<Control-Key-s>", saveNote)
notes.bind("<Control-Key-k>", link)
notes.bind("<Control-Key-o>", openLink)
notes.bind("<Control-slash>", strikethrough)

# Hover Effects
bold.bind("<Enter>", hoverImageBold)
bold.bind("<Leave>", NormalImageBold)
italic.bind("<Enter>", hoverImageItalic)
italic.bind("<Leave>", NormalImageItalic)
underline.bind("<Enter>", hoverImageUnder)
underline.bind("<Leave>", NormalImageUnder)
strikeThrough.bind("<Enter>", hoverImageStrike)
strikeThrough.bind("<Leave>", NormalImageStrike)
bullet.bind("<Enter>", hoverImageBullet)
bullet.bind("<Leave>", NormalImageBullet)
code.bind("<Enter>", hoverImageCode)
code.bind("<Leave>", NormalImageCode)
new.bind("<Enter>", hoverImageNew)
new.bind("<Leave>", NormalImageNew)
save.bind("<Enter>", hoverImageSave)
save.bind("<Leave>", NormalImageSave)
openlink.bind("<Enter>", hoverImageOpen)
openlink.bind("<Leave>", NormalImageOpen)
menu.bind("<Enter>", hoverImageMenu)
menu.bind("<Leave>", NormalImageMenu)
close_button.bind("<Enter>", hoverImageClose)
close_button.bind("<Leave>", NormalImageClose)
insertl.bind("<Enter>", hoverImageLink)
insertl.bind("<Leave>", NormalImageLink)
colorText.bind("<Enter>", hoverImageTsize)
colorText.bind("<Leave>", NormalImageTsize)
photoInsert.bind("<Enter>", hoverImagePhoto)
photoInsert.bind("<Leave>", NormalImagePhoto)

# Desktop Gadget and Autosave
window.after(10, topOrNot)
window.after(3000, autoSave)

# Open a file
if args.file is not None:
    openFile(args.file)

# Update the window
window.mainloop()
