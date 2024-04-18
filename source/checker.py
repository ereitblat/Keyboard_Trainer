import datetime
import time

def check(example, typed, text, stat):
    if example < len(text) and text[example] == typed:
        if example == 0:
            stat.starting_time = time.time()
        if example == len(text) - 1:
            stat.final_time = time.time()
        stat.amount_of_symbols += 1
        stat.current_time = time.time()
        stat.cpm = (stat.amount_of_symbols * 60) // (stat.current_time - stat.starting_time)
        stat.cpm_label.config(text="Amount of symbols per minute: " + str(stat.cpm))
        if typed == " ":
            stat.amount_of_words += 1
            stat.wpm = (stat.amount_of_words * 60) // (stat.current_time - stat.starting_time)
            stat.wpm_label.config(text="Amount of words per minute: " + str(stat.wpm))
        if example == len(text) - 1:
            stat.amount_of_words += 1
            stat.wpm = (stat.amount_of_words * 60) // (stat.current_time - stat.starting_time)
            stat.wpm_label.config(text="Amount of words per minute: " + str(stat.wpm))
            with open("results.txt", "a") as results:
                results.write(str(datetime.date.today()) + "\n" + "Amount of symbols per minute: " + str(
                    stat.cpm) + ", Amount of words per minute: " + str(stat.wpm) + "\n\n")
        return True
    elif 0 < example < len(text):
        stat.amount_of_mistakes+=1
        stat.mistakes_label.config(text="Amount of mistakes: " + str(stat.amount_of_mistakes))
        return "break"
    else:
        return "break"
