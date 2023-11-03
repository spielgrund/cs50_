
with open("name.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
"""
names = []
    
with open("name.txt", "r") as file:
    for line in file:
        	names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
"""
        

"""
with open("name.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
"""

"""
with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

"""