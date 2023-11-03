import re

email = input("Whats your email? ").strip()


#if re.search(r"[a-zA-Z0-9_]+@[az-A-Z0-9_]+\.(com|de|gov|net|edu)$", email, re.IGNORECASE):
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email):
if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")