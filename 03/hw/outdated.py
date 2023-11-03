months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("pls input the date: ").replace("/", " ").replace(","," ").title()
    sdate = date.split()

    if sdate[0].isalpha() and int(sdate[1]) <= 31:
        sdate[0] = months.index(str(sdate[0]))
        sdate[0] = int(sdate[0])+1
        sdate[0] = int(sdate[0])
        sdate[1] = int(sdate[1])
        
        break

    elif sdate[0].isnumeric() and int(sdate[0]) <= 12 and int(sdate[1]) <= 31:
        sdate[0] = int(sdate[0])
        sdate[1] = int(sdate[1])
        
        break
        
    else:
        print("nochmal")




print(f"{sdate[2]:02}",f"{sdate[0]:02}", f"{sdate[1]:02}", sep="-")
