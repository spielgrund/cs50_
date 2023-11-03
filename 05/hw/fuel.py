"""
def main():
    fuel = input("what is the indicator x/y: ")
    percentage = convert(fuel)
    if type(percentage) == int:
        print(gauge(percentage))
"""


def convert(fraction):      #converts x/y into percentage
    while True:
            try:
                x = int(fraction[0])
                #if fuel[1:2] == "/":
                    #print("wrong divisor")
                y = int(fraction[2])
                
                if y == 0:
                    raise ZeroDivisionError ("Y = 0")
                
                if x > y:
                    raise ValueError ("X > Y")
                
                percentage = int(x / y * 100)
                
                
            except (ValueError):
                print("ValueError")
                return ValueError
                #break

            except (ZeroDivisionError):
                print("ZeroDivisionError")
                return ZeroDivisionError
                #break
            
            except (TypeError):
                print("TypeError")
                return TypeError
                #break

            except (AssertionError):
                print("AssertionError")
                return AssertionError
                #break
                
            else:
                return percentage   #should return int

#convert("cat")



def gauge(percentage):
    if type(percentage) == int:
            if 1 < percentage < 98:
                return str(str(percentage) + "%")
                
            elif percentage >= 99:
                return "f"
                
            elif percentage <= 1:
                return "e"
    else:
        return ValueError("not an int")
    

"""
if __name__ == "__main__":
    main()

"""