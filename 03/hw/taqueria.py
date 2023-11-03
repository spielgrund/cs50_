menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
for keys, value in menu.items():
    print(keys, value, "€")

cost = 0
order = []
while True:
    try:
        item = input("Ihre Bestellung bitte: ").title()
        cost += float(menu[item])
        order.append(item)
        
        print(order, "\n", "Gesamt", cost, "€")
    except KeyError:
        print("Keyerror")
    except EOFError:
        print("Vielen Dank für Ihre Bestellung!")
        print("Das macht", cost, "€")
        break
