import random


    
def input_check(s):
    while True:
        try:
            i = int(input(s))
            if i > 0:
                return i
            else:
                print("only positive numbers1")
        except:
            print("only positive numbers2")

a = input_check("Level: ")
a = random.randint(0, a)
b = input_check("Guess: ")
while True:
    if a > b:
        print("too low")
        b = input_check("Guess: ")
    if a < b:
        print("too high")
        b = input_check("Guess: ")
    else:
        print("Correct!")
        break

