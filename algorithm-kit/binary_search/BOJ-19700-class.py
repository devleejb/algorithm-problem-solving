# https://www.acmicpc.net/problem/19700
from sys import stdin
import bisect

input = stdin.readline

N = int(input())
student_list = [list(map(int, input().split())) for _ in range(N)]
student_list.sort(key=lambda s: -s[0])
team_list = []

for student in student_list:
    height, k = student
    right_idx = bisect.bisect_right(team_list, k - 1)

    if right_idx == 0:
        team_list.insert(0, 1)
    else:
        team_list[right_idx - 1] += 1

print(len(team_list))
