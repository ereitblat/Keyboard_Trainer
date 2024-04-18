from myFrame import *
import tkinter
class TextExampleScreen(MyFrame):
    def  __init__(self, window, text):
        super().__init__(window)
        self.example_text = Label(self, text=text,
                                 bg='#EFCFF3',
                                 width=90, height=10,
                                 wraplength=650,
                                 anchor='nw',
                                 justify='left',
                                 padx=5,
                                 pady=5,
                                 relief=tkinter.RAISED,
                                 bd=10,
                                 font="Ariel, 15")
        self.example_text.pack(fill=tkinter.X)


