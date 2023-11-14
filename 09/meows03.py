import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", defualt=1,  help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")