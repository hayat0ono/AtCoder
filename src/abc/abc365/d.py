def main():
    n = int(input())
    s = input()

    dp = [[0 for _ in range(n)] for _ in range(3)]
    if s[0] == 'S':
        dp[0][0] = 1
    elif s[0] == 'P':
        dp[1][0] = 1
    elif s[0] == 'R':
        dp[2][0] = 1

    for i in range(1, n):
        if s[i] == 'S':
            dp[0][i] = max(dp[1][i-1]+1, dp[2][i-1]+1)
            dp[1][i] = max(dp[0][i-1], dp[2][i-1])
        elif s[i] == 'P':
            dp[1][i] = max(dp[0][i-1]+1, dp[2][i-1]+1)
            dp[2][i] = max(dp[0][i-1], dp[1][i-1])
        elif s[i] == 'R':
            dp[0][i] = max(dp[1][i-1], dp[2][i-1])
            dp[2][i] = max(dp[0][i-1]+1, dp[1][i-1]+1)

    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))

if __name__ == '__main__':
    main()