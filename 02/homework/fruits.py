thisdict = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "honeydew": "90",
    "kiwi": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "cherries": "100",
    "tangerine": "50",
    "watermelon": "50",
}
k = input("Fruit: ").lower()
if k in thisdict:
    print("Calories: " + thisdict[k])