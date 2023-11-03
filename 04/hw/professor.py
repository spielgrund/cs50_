import random

list = []


def main():
    level = get_level()
    generate_integer(level)
    print(list)
    
    

def get_level():
    level = input("choose level 1, 2 or 3: ")
    if len(level) == 1 and level.isnumeric and (1 <= int(level) <=3):
        level = int(level)
        print("pass1")
        #generate_integer(level)
        return level
        
    else:
        get_level()


def generate_integer(level):
        if level == 1:
            l = 9
        elif level == 2:
            l = 99
        elif level == 3:
            l = 999
        else:
            raise ValueError("Level must be 1, 2 or 3")
        for _ in range(10):
            a = str(random.randint(0, l))
            b = str(random.randint(0, l))
            aufgabe = str(a + "," + b)
            list.append(aufgabe)
            
            



        print(l)

if __name__ == "__main__":
    main()
    

