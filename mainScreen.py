from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

def runMainScreen():
    mainFrame = Tk()
    topFrame = Frame(mainFrame)
    topFrame.pack()
    listBox = Listbox(topFrame, height =18, width =100, justify = CENTER)
    listBox.pack(side=LEFT)
    scroll = Scrollbar(topFrame, command = listBox.yview)
    listBox.configure(yscrollcommand = scroll.set)
    scroll.pack(side=RIGHT, fill=Y)

    bottomFrame = Frame(mainFrame)
    bottomFrame.pack(side=BOTTOM)
    addButton = Button(bottomFrame,text="PackUp single file",fg="red", command= browse_file)
    addButton.pack(side=LEFT)
    addButton = Button(bottomFrame,text="PackUp whole folder (REQUIRES MORE SPACES)",fg="green", command= browse_folder)
    addButton.pack(side=LEFT)
    mainFrame.mainloop()

def browse_folder():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    #global folder_path
    #folder_path.set(filename)
    #fileLocation = open("folderLocation.txt", "w")
    #fileLocation.write(filename)
    print(filename)

def browse_file():
    #Allow user to search the setting file
    #global folder_path
    settingsFile = askopenfile(title='Open Settings File',filetypes=[('Settings File','*.set')])
    lines = settingsFile.readline()
    #folderLocation = open("folderLocation.txt", "w")
    #folderLocation.write(lines)
    print(lines)

