def main():
    n, k = map(int, input().split())
    s = input()
    l = []
    flag = False
    for i in range(len(s)):
        if not flag and s[i] == '1':
            tmp = [i]
            flag = True
        elif not flag and s[i] == '0':
            continue
        elif flag and s[i] == '1':
            continue
        elif flag and s[i] == '0':
            tmp.append(i-1)
            l.append(tmp)
            flag = False
    if flag:
        l.append(tmp+[len(s)-1])
    ans = s[:l[k-2][1]+1] + s[l[k-1][0]:l[k-1][1]+1] + s[l[k-2][1]+1:l[k-1][0]] + s[l[k-1][1]+1:]
    print(ans)

if __name__ == '__main__':
    main()