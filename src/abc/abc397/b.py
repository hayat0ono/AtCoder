def main():
    s = input()
    perfect_strs = 'io' * 1000
    ans = 0
    now = 0
    for i in range(len(s)):
        if s[i] == perfect_strs[now]:
            now += 1
        else:
            ans += 1
            now += 2
    if s[-1] != 'o':
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()