def solve(n, s, t):
    ans = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] != t[i][j]:
                ans += 1
    return ans


def rotate(n, s):
    ans = []
    for i in range(n):
        ans_tmp = ''
        for j in range(n-1, -1, -1):
            ans_tmp += s[j][i]
        ans.append(ans_tmp)
    return ans


def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        s.append(input())
    for _ in range(n):
        t.append(input())
    ans = solve(n, s, t)
    s = rotate(n, s)
    ans = min(ans, solve(n, s, t) + 1)
    s = rotate(n, s)
    ans = min(ans, solve(n, s, t) + 2)
    s = rotate(n, s)
    ans = min(ans, solve(n, s, t) + 3)
    print(ans)

if __name__ == '__main__':
    main()