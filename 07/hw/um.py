import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    find = re.findall(r"(^um\W*|\sum\W*)",s , re.IGNORECASE)
    return len(find)

if __name__ == "__main__":
    main()