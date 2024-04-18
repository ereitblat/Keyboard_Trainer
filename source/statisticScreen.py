from myFrame import *
from tkinter import *
import time
class StatisticScreen(MyFrame):
    def  __init__(self, window):
        super().__init__(window)
        self.amountOfSymbols = 0
        self.amountOfWords = 0
        self.amountOfMistakes = 0
        self.cpm = 0
        self.wpm = 0
        self.startingTime = 0
        self.finalTime = 0
        self.currentTime = 0
        self.cpmLabel = Label(self, text="Amount of symbols per minute: 0",
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
        self.wpmLabel = Label(self, text="Amount of words per minute: 0",
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
        self.mistakesLabel = Label(self, text="Amount of mistakes: 0",
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
        self.cpmLabel.pack(fill=X)
        self.wpmLabel.pack(fill=X)
        self.mistakesLabel.pack(fill=X)



