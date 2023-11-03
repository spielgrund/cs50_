while True:
    try:
        fuel = input("what is the indicator x/y: ")
        x = int(fuel[0:1])
        #if fuel[1:2] == "/":
            #print("wrong divisor")
        y = int(fuel[2:3])
        gauge = x/y
        
        if gauge > 1:
            print("zu voll")
            
        elif 1 > gauge > 0:
            print(str(gauge*100) + "%")
            break
        elif gauge == 1:
            print("f")
            break
        elif gauge == 0:
            print("e")
            break
    except (ValueError, ZeroDivisionError):
        print("error")

        