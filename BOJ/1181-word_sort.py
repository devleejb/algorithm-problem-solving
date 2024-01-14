from sys import stdin

input = stdin.readline

N = int(input())
word_list = []

for i in range(N):
    word = input().rstrip()
    word_list.append((len(word), word))

word_list = list(set(word_list))
word_list.sort()

for word in word_list:
    print(word[1])
