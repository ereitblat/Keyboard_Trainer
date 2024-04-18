import checker
from textExampleScreen import *
from statisticScreen import *
class TypedTextScreen(MyFrame):
    def  __init__(self, window, generated_text, stat):
        super().__init__(window)
        self.typed_text_screen = Text(self, bg='#D4F3CF', width=90, height=10, padx=5, pady=5, relief=tkinter.RAISED, bd=10, font="Ariel, 15", wrap="word")
        self.typed_text_screen.bind("<Key>", self.key_press)
        self.number_of_typed_screen = 0
        self.generated_text = generated_text
        self.typed_text_screen.pack(fill=tkinter.X)
        self.stat = stat
    def key_press(self, event):
        if (event.char!="Shift") and checker.check(self.number_of_typed_screen, event.char, self.generated_text, self.stat) == True:
            self.number_of_typed_screen+=1
        else:
            return "break"