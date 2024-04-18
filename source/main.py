import tkinter as tk
from typedTextScreen import *
from textExampleScreen import *
from textGenerator import *
from statisticScreen import *
from resultsScreen import *

def StartTyping():
    [child.destroy() for child in window.winfo_children()]
    create_menu()
    generatedText = generate()
    exampleScreen = TextExampleScreen(window, generatedText)
    statisticScreen = StatisticScreen(window)
    typedScreen = TypedTextScreen(window, generatedText, statisticScreen)
    exampleScreen.pack()
    typedScreen.pack()
    statisticScreen.pack()

def Exit():
    [child.destroy() for child in window.winfo_children()]
    create_menu()
    show_info()

def show_results():
    [child.destroy() for child in window.winfo_children()]
    create_menu()
    resultsLabel = ResultsScreen(window)
    resultsLabel.pack()

def create_menu():
    menubar = tk.Menu(window,  bg="#BFE2F1", relief=RAISED, bd=10, activebackground="#BFE2F1")
    window.config(menu=menubar)
    settingsMenu = tk.Menu(menubar, tearoff=0, bg="#BFE2F1")
    settingsMenu.add_command(label="Type", command=StartTyping)
    settingsMenu.add_command(label="Exit", command=Exit)
    settingsMenu.add_command(label="Check results", command=show_results)
    settingsMenu.add_command(label="Finish session", command=window.destroy)
    menubar.add_cascade(label="Menu", menu=settingsMenu, font="Arial, 30")

def show_info():
    textInfo = tk.Label(window, text="For starting typing, click on the menu and choose proper option",
                        font="Arial, 15", width=20, height=6, wraplength=200, bg="#EEE5CB", relief=tkinter.RAISED, bd=10)
    textInfo.place(relx=0.3, rely=0.3)


window = tk.Tk()
window.configure(bg="#B2ABDC")
window.title('Keyboard trainer')
window.geometry("700x700")
window.minsize(700, 700)
window.maxsize(700, 700)
window.resizable(False, False)
create_menu()
show_info()
window.mainloop()
