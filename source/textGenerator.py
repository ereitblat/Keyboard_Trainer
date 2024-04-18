import random
def generate():
    numberOfTheText = random.randint(1, 5)
    with open("../texts/""text" + str(numberOfTheText) + ".txt", mode='rt') as text:
        return text.read()
text = generate()

