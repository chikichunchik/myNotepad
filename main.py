from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tasks import *


def openFile():
    fileName = filedialog.askopenfilename()
    if fileName != "":
        file = open(fileName, "r")
        importText = file.read()
        textArea.delete("1.0", END)
        textArea.insert(END, importText)
        file.close()

def saveToFile():
    fileName = filedialog.askopenfilename()
    if fileName != "":
        text = textArea.get("1.0", END)
        file = open(fileName, "w")
        file.write(text)
        file.close()

def doTask4():
    messagebox.showinfo("Task4", "True" if task4(textArea.get("1.0", END)) else "False")




notepadWindow = Tk()
notepadWindow.title("My notepad")
menuArea = Menu(notepadWindow)
notepadWindow.config(menu=menuArea)
fileMenu = Menu(menuArea)
menuArea.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveToFile)
menuArea.add_command(label="Task4", command=doTask4)

textArea = ScrolledText(notepadWindow)
textArea.pack()
notepadWindow.mainloop()