import csv
import sys
from tabulate import tabulate

pizza = []

if len(sys.argv) < 2:
    print("too few command-line arguments")
    sys.exit()

if len(sys.argv) > 2:
    print("too many command-line arguments")
    sys.exit()

if sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizza.append(row)

        print(tabulate(pizza, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
else:
    print("Not a CSV file")
    sys.exit()