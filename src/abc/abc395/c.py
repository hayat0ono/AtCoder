def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    ans = float('inf')
    for i in range(n):
        if a[i] in d:
            ans = min(ans, i - d[a[i]] + 1)
            d[a[i]] = i
        else:
            d[a[i]] = i
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()