from datetime import date
import inflect
import re
import sys 

def main():
    date = f_vali_date(input("Year of Birth yyyy-mm-dd: "))
    print(f_minutes_to_words(date))



def f_vali_date(i):
    matches = re.search(r"(\d\d\d\d)-(\d\d)-(\d\d)", i)
    if matches:
        if int(matches.group(2)) < 13 and int(matches.group(3)) < 32:
            return i
        else:
            sys.exit("Invalid Date")
            
    else:
        sys.exit("Invalid Date")

def f_minutes_to_words(d):
    p = inflect.engine()
    start = date.fromisoformat(d)
    today = date.today()

    diff = today - start
    days = str(diff).split(" ")
    minutes = int(days[0])*24*60
    words = p.number_to_words(minutes)
    return words

if __name__ == "__main__":
    main()