from tkinter import *

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
    addButton = Button(bottomFrame,text="+",fg="red")
    addButton.pack(side=LEFT)
    mainFrame.mainloop()
