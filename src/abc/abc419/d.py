def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    li = [0] * (n + 1)
    for _ in range(m):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        li[l] += 1
        li[r+1] -= 1
    rev_count = 0
    s_ans = []
    for i in range(n):
        rev_count += li[i]
        if rev_count % 2 == 0:
            s_ans.append(s[i])
        else:
            s_ans.append(t[i])
    print(''.join(s_ans))

if __name__ == '__main__':
    main()