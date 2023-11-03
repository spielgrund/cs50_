def main():
    plate = input("Plate: ")
    is_valid(plate)



def is_valid(s):
    i = 0
    if s.isalnum():         #check for sonderzeichen
        i += 1
        #print("alnum")
    if 2 <= len(s) <= 6:    #check for lengh
        i += 1
        #print("len")
    if s[0:2].isalpha():    #check if first two are letters
        i += 1
        #print("alpha")
    
    if len(s) >= 3:                         #Auf str Länge achten!!! sonst out of index!!!
        if s[2] == "0" and len(s) == 3:     #check1 for zero first
            i -= 1
            #print("is 0 0")
        

    if len(s) >= 4:
        if s[2].isdigit() and s[3].isalpha():     #check1 for no numbers in between letters
            i -= 1
            #print("isnum1")
        if s[2].isdigit() and s[2] == "0" and s[3].isdigit():     #check1 for zero first
            i -= 1
            #print("is 0 1")
        
                   
    if len(s) >= 5:
        if s[3].isdigit() and s[4].isalpha():     #check2 for no numbers in between letters
            i -= 1
            #print("isnum2")  
        if s[3].isdigit() and s[3] == "0" and s[4].isdigit():     #check2 for zero first
            i -= 1
            #print("is 0 2")
        
    if len(s) == 6:
        if s[4].isdigit() and s[5].isalpha():     #check3 for no numbers in between letters
            i -= 1
            #print("isnum3")
        if s[4].isdigit() and s[4] == "0" and s[5].isdigit():     #check2 for zero first
            i -= 1
            #print("is 0 3")
        if s[4].isalpha() and s[5] == "0":     #check3 for zero first
            i -= 1
            #print("is 0 4")


    if i == 3:                                  #checkscore i should be three. Otherwise smth went wrong
        #print(s[2], len(s))
        #print("True")
        return True
    else:
        #print("False")
        return False


if __name__ == "__main__":
    main()