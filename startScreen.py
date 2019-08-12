from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    fileLocation = open("folderLocation.txt", "w")
    fileLocation.write(filename)
    print(filename)

def browse_file():
    #Allow user to search the setting file
    global folder_path
    settingsFile = askopenfile(title='Open Settings File',filetypes=[('Settings File','*.set')])
    lines = settingsFile.readline()
    folderLocation = open("folderLocation.txt", "w")
    folderLocation.write(lines)
    print(lines)

def runMainScreen():
    mainFrame = Tk()
    folder_path = StringVar()
    topFrame = Frame(mainFrame, width=100, height=100)
    topFrame.pack()

    chooseFolderButton = Button(topFrame, text= "Choose back up location", fg= "red", command=browse_button)
    loadSettingsButton = Button(topFrame, text= "Choose settings file", fg= "green", command=browse_file)
    chooseFolderButton.pack()
    loadSettingsButton.pack()
    mainFrame.mainloop()

