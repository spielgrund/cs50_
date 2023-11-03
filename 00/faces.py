def main():
    faces = input("Input: ")
    n = convert(faces)
    print(n)
    

def convert(faces):
    faces = faces.replace(":)", "🙂")
    faces = faces.replace(":(", "🙁")
    return faces


main()

