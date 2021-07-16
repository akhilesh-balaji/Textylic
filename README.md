# Textylic

![Textylic: the notes app for the 22nd century](https://github.com/akhilesh-balaji/Textylic/blob/master/res/images/mockups/Mockup.png?raw=true)

This is **Textylic**—the notes app for the 22nd century. It supports various formatting options including **bold**, *italic*, <ins>underline</ins>, `code`, and ~~strikethrough~~. The app also supports other formats such as bullet points, and hyperlinks. You can also open links in your browser! You can customize the app by changing the theme, too! Unlike the native windows sticky notes app, this app stays on your desktop like a windows 7 widget, without the need to install any large and cumbersome software such as Rainmeter. This means that it won't interfere with your work by creating icons on the taskbar that you need to click on to open. Textylic also supports  multiple note windows, and scrolling. So, you are not limited to the default square window size.

<!-- As of now, there are a few bugs. Here are a couple of the known bugs that I am working on fixing:
N/A -->

You can download from the [GitHub releases page](https://github.com/akhilesh-balaji/Textylic/releases)

Upvote this product on [ProductHunt](https://www.producthunt.com/posts/textylic)

## Features

- **Windows 7-esque desktop widget**: Remember those useful desktop widgets in windows 7? These were interactive features in the desktop that didn't interfere with your work by showing up in the taskbar. Instead, they stayed on the desktop, and if you minimized all the maximized windows, you could interact with them These were removed in Windows 10. But, this app mimics their behaviour, and has a modern notes window that stays on the desktop. This has a lot of features extended from the default windows 10 sticky notes app, and some completely new ones, too!

- **New Window**: Textylic has the ability to create multiples notes windows on the same desktop. This is a particularly useful feature when taking notes during meetings or class. They can also be organized by use of other features in the app such as colour coding. These individual notes windows don't interfere with each other in any way, and you can even edit the same note in two different windows at the same time!
This can be accessed by clicking the plus icon in the top toolbar.

- **Text formatting Options**: Plaintext, at times, gets too boring, and it's hard to emphasize text. When a notes app doesn't support these, it means that you have to rely on online text to Unicode formatting convertors. But fear not, for Textylic supports over 7 types of text formatting, with more coming soon!

- **Colour Themes**: Using colour themes, you can both customize the appearance of Textylic, and organize yourself by colour coding the notes. There are 4 colour options available as of now. This feature can also be combined with other features, such as naming and renaming your notes, to better organize your note-taking experience. After all, nothing's better than a splash of colour on your desktop!

- **Links**: You can link piece of text by selecting it, and using <kbd>Ctrl + O</kbd> on the keyboard, or using the formatting toolbar icon. To open the link, select the link, and use <kbd>Ctrl + O</kbd>, or the "Open selected link" option in the top toolbar.

- **Automatic Saving**: This is quite a handy tool if your computer suddenly crashed, and you have unsaved work. You only need to save a note once, to choose its location and name. Then, Textylic will automatically save it every half a second or so. It also saves you the trouble of hitting Ctrl + S every time you made a change, and wearing those keys down to the plastic underneath.

## Keyboard Shortcuts

- **<kbd>Ctrl + Z</kbd>**: Undo
- **<kbd>Ctrl + Y</kbd>**: Redo
- **<kbd>Ctrl + K</kbd>**: Add a hyperlink to a selected object
- **<kbd>Ctrl + O</kbd>**: Open the selected hyperlink in default web browser
- **<kbd>Ctrl + B</kbd>**: Make selected text bold
- **<kbd>Ctrl + I</kbd>**: Make selected text italic
- **<kbd>Ctrl + U</kbd>**: Make selected text underlined
- **<kbd>Ctrl + Q</kbd>**: Quit the program. Use this when you close the last notes window, or it will keep running in the background, and you need to end it using task manager.
- **<kbd>Ctrl + S</kbd>**: Save the file

## Usage

### Installation

#### Portable

Download `textylic-portable-x64.zip` from the [releases page](https://github.com/akhilesh-balaji/Textylic/releases) and extract its contents to a safe place. Run `Textylic.exe`.

#### Installer

Download `textylic-setup-x64.exe` from the [releases page](https://github.com/akhilesh-balaji/Textylic/releases) and open the file, following the instructions.

#### Running From Source

Download the source code or clone this repository. Install `pygetwindow` and `pil` using python `pip`. Next, run `main.py`. This is the notes window.

### Using the application

<img title="" src="https://raw.githubusercontent.com/akhilesh-balaji/Textylic/master/res/images/Tutorial.png" alt="" width="373" height="">

#### 1. The **New Note** Button

This button creates a new note in a separate window. This way, you can have multiple notes on your desktop!

#### 2. The **Save Note** Button

This is the button that saves your work. You can either use this button,or the keyboard shortcut <kbd>Ctrl + S</kbd>. You only need to do this the first time, because of the Autosave feature.

#### 3. The **Open Selected Link** Button

If you have a link selected,you can click this button to open this link in the browser.This only works if you have tagged your text as a link in the bottom bar (See 12)

#### 4. The **Extended Menu** Button

This button opens up the extended menu, with a few more features. One of the most prominent is the "Choose theme" option, which allows you to customize the interface. You can also find the Undo/Redo buttons here, though they can also be accessed through the keyboard shortcuts (see above). You can also get help and learn more about the app through the Help/About buttons.

#### 5. The **Close Window** Button

This is self-explanatory. If you click this button, it closes the window. Each window is a separate instance of the .exe file, so <kbd>Ctrl + Q</kbd> will do the same as this button.

#### 6. The **Bold** Button

This button makes the selected text bold.

#### 7. The **Italic** Button

This button makes the selected text italic.

#### 8. The **Underline** Button

This button makes the selected text underlined.

#### 9. The **Strikethrough** Button

This button makes the selected text strikethrough.

#### 10. The **Bulleted List** Button

This button adds turns the selected lines into a bulleted list.

#### 11. The **Code** Button

This button makes the selected text look like code, by using a fixed-width font.

#### 12. The **Hyperlink** Button

This button makes the selected text a hyperlink. To open it, see 3.

#### 13. The **Colour** Button

This button emphasizes the selected text by turning it the colour of your chosen theme.

#### 14. The **Image** Button

This button will insert a desired image in the position where you insertion cursor is. Clear the images that are not used using the "Clear Cache" option in the "More..." menu.

## Requirements

- Windows 10 version 1903 or higher
- Windows 8 and below have not been tested, but are supported

## Roadmap of Features

**Note:** If you have any features that are not on this list, or any bugs to report, please do not hesitate to create a new issue in the "Issues" tab above. The items which have a version number next to them are planned for that release number, the others will be updated soon.

| Feature                           | Progress | Notes                                                        |
|:----------------------------------|:--------:|--------------------------------------------------------------|
| Refine Desktop Widget             |   10%    | I made a few attempts at this, but they didn't work out well |
| Spell Checker                     |    0%    | This is long-term                                            |
| Open Note by clicking on the file |    0%    | Help Wanted                                                  |

## Screenshot

![Screenshot](https://github.com/akhilesh-balaji/Textylic/blob/master/res/images/screenshot.png?raw=true)
