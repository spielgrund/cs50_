tweet = input("input: ")
tweet2 = tweet
twttr = ""

vokale = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for e in tweet:
    if e not in vokale:
        twttr += e

for e in tweet:
    if e in vokale:
        tweet2 = tweet2.replace(e, "")
    

print(twttr)
print(tweet2)


