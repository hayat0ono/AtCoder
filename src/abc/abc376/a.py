def main():
    n, c = map(int, input().split())
    t = list(map(int, input().split()))
    ans = 1
    bef = t[0]
    for i in range(1, n):
        if t[i] - bef >= c:
            ans += 1
            bef = t[i]
    print(ans)

if __name__ == '__main__':
    main()