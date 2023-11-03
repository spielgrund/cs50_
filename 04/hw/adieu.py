import inflect

ie = inflect.engine()
l = []

while True:
    try:
        item = input("Add items: ")
        l.append(item)
    except EOFError:
        l = ie.join(l)
        print("Adieu, adieu, to ", l)
        break


"""
mylist = ie.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot"
print(mylist)
"""