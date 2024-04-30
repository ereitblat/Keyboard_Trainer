from myFrame import *
from tkinter import *
class StatisticScreen(MyFrame):
    def  __init__(self, window):
        super().__init__(window)
        self.amount_of_symbols = 0
        self.amount_of_words = 0
        self.amount_of_mistakes = 0
        self.cpm = 0
        self.wpm = 0
        self.starting_time = 0
        self.final_time = 0
        self.current_time = 0
        self.cpm_label = Label(self, text="Amount of symbols per minute: 0",
                                 bg='#F5E5E0',
                                 width=90, height=1,
                                 wraplength=600,
                                 anchor='nw',
                                 justify='center',
                                 padx=5,
                                 pady=5,
                                 relief=RAISED,
                                 bd=10,
                                 font="Ariel, 15")
        self.wpm_label = Label(self, text="Amount of words per minute: 0",
                         bg='#F5E5E0',
                         width=90, height=1,
                         wraplength=600,
                         anchor='nw',
                         justify='center',
                         padx=5,
                         pady=5,
                         relief=RAISED,
                         bd=10,
                         font="Ariel, 15")
        self.mistakes_label = Label(self, text="Amount of mistakes: 0",
                              bg='#F5E5E0',
                              width=90, height=1,
                              wraplength=600,
                              anchor='nw',
                              justify='center',
                              padx=5,
                              pady=5,
                              relief=RAISED,
                              bd=10,
                              font="Ariel, 15")
        self.cpm_label.pack(fill=X)
        self.wpm_label.pack(fill=X)
        self.mistakes_label.pack(fill=X)



