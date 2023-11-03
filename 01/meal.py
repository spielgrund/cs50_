#input time > convert > print time
def main():
    time = input("wieviel Uhr möchten Sie essen? ")
    fhours, fminutes = convert(time)
    combi = fhours+fminutes
    if 7 <= combi < 8:
        print("Breakfast")
    elif 12 <= combi < 13:
        print("Lunch")
    elif 18 <= combi < 19:
        print("Dinner")
    else:
        pass

    

#converts string of hoours in float
def convert(time):
    hours, minutes = time.split(":")
    fhours = float(hours)
    fminutes = float(minutes)
    fminutes = fminutes/60
    return fhours, fminutes
    


if __name__ == "__main__":
    main()