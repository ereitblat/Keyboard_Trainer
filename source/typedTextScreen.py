import checker
from textExampleScreen import *
from statisticScreen import *
class TypedTextScreen(MyFrame):
    def  __init__(self, window, generatedText, stat):
        super().__init__(window)
        self.typedTextScreen = Text(self, bg='#D4F3CF', width=90, height=10, padx=5, pady=5, relief=tkinter.RAISED, bd=10, font="Ariel, 15")
        self.typedTextScreen.bind("<Key>", self.key_press)
        self.numberOfTypedScreen = 0
        self.generatedText = generatedText
        self.typedTextScreen.pack(fill=tkinter.X)
        self.stat = stat
    def key_press(self, event):
        if (event.char!="Shift") and checker.check(self.numberOfTypedScreen, event.char, self.generatedText, self.stat) == True:
            self.numberOfTypedScreen+=1
        else:
            return "break"