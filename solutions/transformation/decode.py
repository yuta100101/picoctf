import sys

filename = sys.argv[1]
with open(filename, "r") as f:
    encoded_string = f.read()

decoded_chars = []
for i in range(len(encoded_string)):
    decoded_chars.append(chr(ord(encoded_string[i])>>8))
    decoded_chars.append(chr((ord(encoded_string[i]))-((ord(encoded_string[i])>>8)<<8)))

print("".join(decoded_chars))

