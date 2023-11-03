import random



def main():
    level = get_level()
    score = 0
    for _ in range(10):
        a , b = generate_integer(level)
        t = 1
        
        while t <= 3:
            try:
                frage = str(str(a) + " + " + str(b) + " = ")
                ergebniss = int(input(str(frage)))
                if ergebniss == (a+b):
                    score += 1
                    break
                elif t == 3:
                    print(a,"+",b ,"=", (a+b))
                    t = 1
                    break
                else:
                    print("EEE")
                    t += 1
            except ValueError:
                print("value error")
                print("EEE")
                t += 1
                
            
    print(score)
            
        
    
    
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
        a = random.randint(0, l)
        b = random.randint(0, l)
        return a,b       
            


if __name__ == "__main__":
    main()
    

