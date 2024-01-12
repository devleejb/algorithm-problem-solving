word = input()
alphabet = [[0, chr(i + 97)] for i in range(26)]

for c in word.lower():
    alphabet[ord(c) - 97][0] += 1

alphabet.sort()
if alphabet[24][0] == alphabet[25][0]:
    print("?")
else:
    print(alphabet[25][1].upper())
