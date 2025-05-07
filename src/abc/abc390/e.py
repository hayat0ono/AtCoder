def main():
    n, x = map(int, input().split())
    v1 = []
    v2 = []
    v3 = []
    for _ in range(n):
        v, a, c = map(int, input().split())
        if v == 1:
            v1.append([a, c])
        elif v == 2:
            v2.append([a, c])
        else:
            v3.append([a, c])         
    dp_1 = [0] * (x+1)
    dp_2 = [0] * (x+1)
    dp_3 = [0] * (x+1)
    for a, c in v1:
        for i in range(x, c-1, -1):
            dp_1[i] = max(dp_1[i], dp_1[i-c] + a)
    for a, c in v2:
        for i in range(x, c-1, -1):
            dp_2[i] = max(dp_2[i], dp_2[i-c] + a)
    for a, c in v3:
        for i in range(x, c-1, -1):
            dp_3[i] = max(dp_3[i], dp_3[i-c] + a)

    def get_cost(dp, m):
        for i in range(x+1):
            if dp[i] >= m:
                return i
        return -1
    
    left, right = 0, min(sum(a for a, c in v1), sum(a for a, c in v2), sum(a for a, c in v3))
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        cost_1 = get_cost(dp_1, mid)
        cost_2 = get_cost(dp_2, mid)
        cost_3 = get_cost(dp_3, mid)
        if cost_1 != -1 and cost_2 != -1 and cost_3 != -1:
            if cost_1 + cost_2 + cost_3 <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        else:
            right = mid - 1
    print(ans)

if __name__ == '__main__':
    main()