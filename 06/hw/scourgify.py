import csv
import sys
import os.path


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit()

if os.path.isfile(sys.argv[1]):
    pass
else:
    print("Could not read " + sys.argv[1])


if sys.argv[1].endswith(".csv") and sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1], newline="") as rein, open (sys.argv[2], "a", newline="") as raus:
            reader = csv.DictReader(rein)
            writer = csv.DictWriter(raus, fieldnames=["first_name","last_name","house"])
            #writer.writeheader("first_name","last_name","house")
            for row in reader:
                split = row["name"].split(",")
                first_name = split[1]
                last_name = split[0]
                writer.writerow({"first_name": first_name, "last_name": last_name, "house": row["house"]})
    except:
        pass
            
