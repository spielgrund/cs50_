def main():
    word = input("input: ")
    word = shorten(word)
    print(word)
    


def shorten(word):
    vokale = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for v in word:
        if v in vokale:
            word = word.replace(v, "")
    return word
        


if __name__ == "__main__":
    main()

