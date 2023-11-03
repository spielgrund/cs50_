camel = input("camelcase: ")
result = ""
#l = list(camel)
for e in camel:
    if e.isupper():
        result += str("_" + e.lower())
    else:
        result += e

print("snake_case: " + result)
