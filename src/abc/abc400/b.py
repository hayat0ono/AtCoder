def main():
    n, m = map(int, input().split())
    ans = 0
    now = 1
    for i in range(0, m+1):
        ans += now
        now = now * n
        if ans > 10**9:
            print('inf')
            return
    print(ans)

if __name__ == '__main__':
    main()