def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0][0] = a[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + a[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + 2*a[i])
    print(max(dp[-1]))


if __name__ == '__main__':
    main()