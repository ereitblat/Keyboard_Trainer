import tkinter as tk
from typedTextScreen import *
from textExampleScreen import *
from textGenerator import *
from statisticScreen import *
from resultsScreen import *

def start_typing():
    [child.destroy() for child in window.winfo_children()]
    create_menu()
    generated_text = generate()
    example_screen = TextExampleScreen(window, generated_text)
    statistic_screen = StatisticScreen(window)
    typed_screen = TypedTextScreen(window, generated_text, statistic_screen)
    example_screen.pack()
    typed_screen.pack()
    statistic_screen.pack()

def exit_from_typing():
    [child.destroy() for child in window.winfo_children()]
    create_menu()
    show_info()

def show_results():
    [child.destroy() for child in window.winfo_children()]
    create_menu()
    results_label = ResultsScreen(window)
    results_label.pack()

def create_menu():
    menubar = tk.Menu(window,  bg="#BFE2F1", relief=RAISED, bd=10)
    window.config(menu=menubar)
    settings_menu = tk.Menu(menubar, tearoff=0, bg="#BFE2F1")
    settings_menu.add_command(label="Type", command=start_typing)
    settings_menu.add_command(label="Exit", command=exit_from_typing)
    settings_menu.add_command(label="Check results", command=show_results)
    settings_menu.add_command(label="Finish session", command=window.destroy)
    menubar.add_cascade(label="Menu", menu=settings_menu, font="Arial, 30")

def show_info():
    text_info = tk.Label(window, text="For starting typing, click on the menu and choose proper option",
                        font="Arial, 15", width=20, height=6, wraplength=200, bg="#EEE5CB", relief=tkinter.RAISED, bd=10)
    text_info.place(relx=0.3, rely=0.3)


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
