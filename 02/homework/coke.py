
due = 50
while due > 0:
    print("Amount Due: " + str(due))
    amt = int(input("insert coin: "))
    if amt == 25 or amt == 10 or amt == 5:
        due -= amt
    else: print("Wrong Coin!")
    if due <= 0:
        print("Change Owed: " + str(-due))

