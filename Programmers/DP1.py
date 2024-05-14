def solution(N, number):
    answer = -1
    dp = [set() for _ in range(9)]
    
    concat_N = N
    
    for num_cnt in range(1, 9):
        dp[num_cnt].add(concat_N)
        concat_N = concat_N * 10 + N
        for first in range(1, num_cnt):
            second = num_cnt - first
            for val1 in dp[first]:
                for val2 in dp[second]:
                    dp[num_cnt].add(val1 + val2)
                    dp[num_cnt].add(val1 - val2)
                    dp[num_cnt].add(val1 * val2)
                    if val2 != 0:
                        dp[num_cnt].add(val1 // val2)
        
        if number in dp[num_cnt]:
            answer = num_cnt
            break
    
    return answer