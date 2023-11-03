glist= {}

while True:
    try:
        item = input("Add items: ").title()
        if item not in glist.keys():
            glist[item] = 1
        else:
            glist[item] += 1
    except KeyError:
        print("wrong input")
    except EOFError:
        for keys, value in glist.items():
            print(value, keys)
        break