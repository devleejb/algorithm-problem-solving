def MinWindowSubstring(strArr):
    N, K = strArr
    chars = set(list(K))
    visited = {}
    visited_len = 0
    min_window_substring = N

    for i in range(len(N)):
        # Clear Visited
        visited_len = 0
        for c in chars:
            visited[c] = False

        for j in range(i, len(N)):
            if N[j] not in visited:
                continue

            if not visited[N[j]]:
                visited_len += 1
                visited[N[j]] = True

            if visited_len == len(chars):
                if len(min_window_substring) > j - i + 1:
                    min_window_substring = N[i : j + 1]
                break

    # code goes here
    return min_window_substring


# keep this function call here
print(MinWindowSubstring(input()))
