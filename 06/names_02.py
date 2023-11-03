name = input("Whats your name?: ")

file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()