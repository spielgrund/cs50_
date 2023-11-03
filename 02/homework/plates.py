def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    if s.isalnum():
        i += 1
        print("alnum")
    if 6 >= len(s) >= 2:
        i += 1
        print("len")
    if s[0:2].isalpha():
        i += 1
        print("alpha")
    if i == 3:
        return True
    else: return False
    


main()


"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
isalpha()
isdigit()
"""