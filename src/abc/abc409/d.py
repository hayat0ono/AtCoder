def solve(n, s):
    ans = s
    for i in range(n - 1):
        now = s[i]
        if now > s[i+1]:
            for j in range(i+1, n):
                if now < s[j]:
                    ans = s[:i] + s[i+1:j] + s[i] + s[j:]
                    print(ans)
                    return
                elif j == n-1:
                    ans = s[:i] + s[i+1:] + s[i]
                    print(ans)
                    return
    print(ans)



def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        solve(n, s)


if __name__ == '__main__':
    main()