def main():
    n, d = map(int, input().split())
    ans = [float('-inf') for _ in range(d)]
    for _ in range(n):
        t, l = map(int, input().split())
        for k in range(1, d+1):
            ans[k-1] = max(ans[k-1], t*(l+k))
    for i in range(d):
        print(ans[i])

if __name__ == '__main__':
    main()