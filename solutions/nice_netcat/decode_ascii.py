import sys

filename = sys.argv[1]
with open(filename, "r") as f:
    data = f.readlines()

print("".join([chr(int(d)) for d in data]))
