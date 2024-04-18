import datetime

from statisticScreen import *


def check(example, typed, text, stat):
    if example < len(text) and text[example] == typed:
        if example == 0:
            stat.startingTime = time.time()
        if example == len(text) - 1:
            stat.finalTime = time.time()
        stat.amountOfSymbols += 1
        stat.currentTime = time.time()
        stat.cpm = (stat.amountOfSymbols * 60) // (stat.currentTime - stat.startingTime)
        stat.cpmLabel.config(text="Amount of symbols per minute: " + str(stat.cpm))
        if (typed == " " ):
            stat.amountOfWords += 1
            stat.wpm = (stat.amountOfWords * 60) // (stat.currentTime - stat.startingTime)
            stat.wpmLabel.config(text="Amount of words per minute: " + str(stat.wpm))
        if (example == len(text) - 1):
            stat.amountOfWords += 1
            stat.wpm = (stat.amountOfWords * 60) // (stat.currentTime - stat.startingTime)
            stat.wpmLabel.config(text="Amount of words per minute: " + str(stat.wpm))
            with open("results.txt", "a") as results:
                results.write(str(datetime.date.today()) + "\n" + "Amount of symbols per minute: " + str(
                    stat.cpm) + ", Amount of words per minute: " + str(stat.wpm) + "\n\n")
        return True
    elif example < len(text) and example > 0:
        stat.amountOfMistakes+=1
        stat.mistakesLabel.config(text="Amount of mistakes: " + str(stat.amountOfMistakes))
        return "break"
    else:
        return "break"
