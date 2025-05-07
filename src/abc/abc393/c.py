def main():
    n, m = map(int, input().split())
    g = {}
    for i in range(n):
        g[i] = []
    ans = 0
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if u in g[v] and v in g[u]:
            ans += 1
        elif u == v:
            ans += 1
        else:
            g[u].append(v)
            g[v].append(u)
    print(ans)

if __name__ == '__main__':
    main()