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

def doTask7():
    messagebox.showinfo("Task7", "True" if task7(textArea.get("1.0", END)) else "False")

def doTask11():
    messagebox.showinfo("Task11", task11(textArea.get("1.0", END)))

def doTask36():
    messagebox.showinfo("Task36", "True" if task36(textArea.get("1.0", END)) else "False")

def doTask2():
    messagebox.showinfo("Task2", task2(textArea.get("1.0", END)))

def doTask31():
    text_in_area = textArea.get("1.0", END)
    textArea.delete("1.0", END)
    textArea.insert("1.0", task31(text_in_area))

def doTask48():
    text_in_area = textArea.get("1.0", END)
    textArea.delete("1.0", END)
    textArea.insert("1.0", task48(text_in_area))

notepadWindow = Tk()
notepadWindow.title("My notepad")
menuArea = Menu(notepadWindow)
notepadWindow.config(menu=menuArea)
fileMenu = Menu(menuArea)
menuArea.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveToFile)
menuArea.add_command(label="Task4", command=doTask4)
menuArea.add_command(label="Task7", command=doTask7)
menuArea.add_command(label="Task11", command=doTask11)
menuArea.add_command(label="Task36", command=doTask36)

textArea = ScrolledText(notepadWindow, bd=0)
textArea.pack(fill=BOTH, expand=True)
notepadWindow.mainloop()
