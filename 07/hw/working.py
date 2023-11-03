import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"([0-9][0-9]?:?[0-5]?[0-9]?) (AM|PM) to ([0-9][0-9]?:?[0-5]?[0-9]?) (AM|PM)" , s)
    if matches:
        try:         
            if ":" in matches.group(1) and matches.group(2) == "PM":
                split_g1 = matches.group(1).split(":")
                first_g1 = int(split_g1[0])+12
                first = str(first_g1) + ":" + split_g1[1]
            
            if ":" not in matches.group(1) and matches.group(2) == "PM":
                first = int(matches.group(1))+12
                first = str(first) + ":00"

            if ":" in matches.group(1) and matches.group(2) == "AM":
                first = matches.group(1)

            if ":" not in matches.group(1) and matches.group(2) == "AM":
                first = matches.group(1) + ":00"

            if ":" in matches.group(3) and matches.group(4) == "PM":
                split_g3 = matches.group(3).split(":")
                second_g3 = int(split_g3[0])+12
                second = str(second_g3) + ":" + split_g3[1]
            
            if ":" not in matches.group(3) and matches.group(4) == "PM":
                second = int(matches.group(3))+12
                second = str(second) + ":00"

            if ":" in matches.group(3) and matches.group(4) == "AM":
                second = matches.group(3)

            if ":" not in matches.group(3) and matches.group(4) == "AM":
                second = matches.group(3) + ":00"

            """
            print(matches.group(1))
            print(matches.group(2))
            print(matches.group(3))
            print(matches.group(4))
            print("############################")
            print(first)
            print(second)
            """
            final = first + " to " + second
            return final
        
        except ValueError:
            return ValueError("Wrong Input")
            
    else:
        return ValueError("Wrong Input")


"""
 Type 9 AM to 5 PM, followed by Enter. Your program should output 09:00 to 17:00.
 Type 9:00 AM to 5:00 PM, followed by Enter. Your program should again output 09:00 to 17:00.
 Type 10 PM to 8 AM, followed by Enter. Your program should output 22:00 to 08:00.
 Type 10:30 PM to 8:50 AM, followed by Enter. Your program should again output 22:30 to 08:50.
 Try intentionally inducing a ValueError by typing 9:60 AM to 5:60 PM, followed by Enter. Your program should indeed raise a ValueError.
 Try intentionally inducing a ValueError by typing 9 AM - 5 PM, followed by Enter. Your program should indeed raise a ValueError.
 Try intentionally inducing a ValueError by typing 09:00 AM - 17:00 PM, followed by Enter. Your program should indeed raise a ValueError.
"""


if __name__ == "__main__":
    main()