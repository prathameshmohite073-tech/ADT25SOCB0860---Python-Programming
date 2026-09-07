def lcs(X: str, Y: str):
    m, n = len(X), len(Y)

    # Initialize table with zeros
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill DP table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the actual LCS string
    lcs_chars = []
    i, j = m, n

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_chars.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the characters because we backtracked from the end
    lcs_chars.reverse()

    return dp[m][n], "".join(lcs_chars)


# Example usage
length, subsequence = lcs("stone", "longest")

print(f"Length: {length}")
print(f"Subsequence: '{subsequence}'")
