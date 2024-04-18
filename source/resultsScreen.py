from myFrame import *
import tkinter
class ResultsScreen(MyFrame):
    def  __init__(self, window):
        super().__init__(window)
        with open("results.txt", "r") as results:
            self.resultsScreen = Canvas(self,scrollregion=(0, 0, 3000, 3000),
                                 bg='light green',
                                 width=665, height=400,
                                 relief=tkinter.RAISED,
                                 bd=5)
            self.resultsScreen.pack()
            self.scrollbar = Scrollbar(self, orient=VERTICAL)
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.scrollbar.config(command=self.resultsScreen.yview)
            self.resultsScreen.create_text(8, 8, text=results.read(), anchor='nw', justify='left', font="Ariel 13")
            self.scrollbar["command"]=self.resultsScreen.yview
            self.resultsScreen.config(yscrollcommand=self.scrollbar.set)
            self.resultsScreen.pack(side=LEFT, expand=True, fill=BOTH)
            # scrollbar = Scrollbar(self.resultsScreen, orient='vertical', command=self.yview(), activebackground="light blue", troughcolor="light blue")
            # self.resultsScreen.pack(side=LEFT, fill=tkinter.Y)
            # scrollbar.pack(side=RIGHT, fill=Y)