greeting = input("Greeting?: ").lower().strip()
greeting_words = greeting.split()

if greeting_words[0] == "hello":
    print("0€") 
elif greeting_words[0] == "hello,":
    print("0€") 
elif greeting[0] == "h":
    print("20€")
else:
    print("100€")