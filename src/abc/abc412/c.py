import bisect

def solve(n, s):
    now = s[0]
    end = s[-1]
    s.sort()
    ans = 2
    while 2 * now < end:
        index = bisect.bisect_right(s, 2 * now)
        if now == s[index-1]:
            print(-1)
            return
        now = s[index-1]
        ans += 1
    print(ans)
    return


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        solve(n, s)


if __name__ == '__main__':
    main()