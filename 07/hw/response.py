from validator_collection import validators, errors

def main():
    print(email_validate(input("Email: ")))

def email_validate(e):
    try:
        email_address = validators.email(e)
        return "Valid"
        # Will raise an EmptyValueError
    except errors.EmptyValueError:
        return "Invalid"
        # Handling logic goes here
    except errors.InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()
