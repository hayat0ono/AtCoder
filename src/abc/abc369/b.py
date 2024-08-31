def main():
    n = int(input())
    ans = 0
    now_l, now_r = -1, -1
    for _ in range(n):
        a, s = input().split()
        a = int(a)
        if s == 'L':
            if now_l == -1:
                now_l = a
            else:
                ans += abs(a-now_l)
                now_l = a
        elif s == 'R':
            if now_r == -1:
                now_r = a
            else:
                ans += abs(a-now_r)
                now_r = a
    print(ans)


if __name__ == '__main__':
    main()