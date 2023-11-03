import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    matches = re.search(r"^(\d\d?\d?)\.(\d\d?\d?)\.(\d\d?\d?)\.(\d\d?\d?)$", ip)
    if matches:
        gr1 = int(matches.group(1))
        gr2 = int(matches.group(2))
        gr3 = int(matches.group(3))
        gr4 = int(matches.group(4))
        #print(gr1,gr2,gr3,gr4)
        if (0 <= gr1 <= 255) and (0 <= gr2 <= 255) and (0 <= gr3 <= 255) and (0 <= gr4 <= 255):
            return True
        else:
            return False
    else:
        return False





if __name__ == "__main__":
    main()