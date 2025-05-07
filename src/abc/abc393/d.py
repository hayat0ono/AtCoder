def main():
    n = int(input())
    s = input()
    p = [i for i, c in enumerate(s) if c == '1']
    cnt_1 = len(p)
    q = [p[i] - i for i in range(cnt_1)]
    med = q[cnt_1 // 2]
    ans = 0
    for i in q:
        ans += abs(i - med)
    print(ans)

if __name__ == '__main__':
    main()