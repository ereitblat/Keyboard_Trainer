import random
import os
def generate():
    number_of_the_text = random.randint(1, 5)
    with open("../texts/""text" + str(number_of_the_text) + ".txt", mode='rt') as text:
        return text.read()
text = generate()

