def main():
    n, q = map(int, input().split())
    li = []
    for i in range(q):
        h, t = input().split()
        if h == 'L':
            h = 0
        else:
            h = 1
        t = int(t)
        li.append([h, t])
    now = [1, 2]
    ans = 0
    for i in range(q):
        mov = li[i][0]
        ano = 1 - mov
        if not now[ano] in range(min(now[mov], li[i][1]), max(now[mov], li[i][1]) + 1):
            ans += abs(now[mov] - li[i][1])
            now[mov] = li[i][1]
        else:
            ans += n - abs(now[mov] - li[i][1])
            now[mov] = li[i][1]
    print(ans)

if __name__ == '__main__':
    main()