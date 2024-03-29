from sys import stdin

input = stdin.readline

N = int(input())
member_list = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    member_list.append([age, name])

member_list.sort(key=lambda m: m[0])

for member in member_list:
    print(*member)
