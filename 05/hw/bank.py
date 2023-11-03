def main():
    greeting = input("Greeting: ")
    v = value(greeting)
    print(v)


def value(greeting):
    greeting = greeting.lower()
    greeting_split = greeting.split()
    if greeting_split[0] == "hello":
         return 0 
    elif greeting_split[0] == "hello,":
         return 0
    elif greeting[0] == "h":
         return 20
    else:
        return 100


if __name__ == "__main__":
    main()