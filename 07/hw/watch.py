import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"youtube\.com/embed/", s):
        matches = re.search(r"(src=\")(http://|https://)(www\.)?(youtube\.com/embed/)(\w*)\"", s)
        if matches.group(5):
            return str("https://youtu.be/" + matches.group(5))
            
        else:
            return None



if __name__ == "__main__":
    main()