# https://www.acmicpc.net/problem/2212
# 1. 핵심 아이디어 추론
#    센서 사이의 거리가 먼 곳부터 연결을 지워나간다.
# 2. 정당성 분석
#    전체 합에서 가장 긴 것을 지우는 것보다 더 짧게 만들 수 없다.
from sys import stdin

input = stdin.readline

N = int(input())
K = int(input())
pos_list = list(map(int, input().split()))
pos_list.sort()

dis_list = [pos_list[i] - pos_list[i - 1] for i in range(1, N)]
dis_list.sort()

print(sum(dis_list[0 : len(dis_list) - K + 1]))
