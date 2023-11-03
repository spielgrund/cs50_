def main():

    x = float(input("whats x?"))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2)

main()