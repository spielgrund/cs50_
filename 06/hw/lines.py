import sys

if len(sys.argv) < 2:
    print("too few command-line arguments")
    sys.exit()

if len(sys.argv) > 2:
    print("too many command-line arguments")
    sys.exit()

if sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            total_lines = len(lines)
            comments = 0
            empty = 0
            for l in lines:
                a = l.strip()
                if a.startswith("#"):
                    comments += 1
                #print(l.strip())
                if not a:               #check if string is empty
                    empty += 1
                #if l == "":
                #    print("_")
            print(total_lines-comments-empty)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
else:
    print("Not a Python file")
    sys.exit()