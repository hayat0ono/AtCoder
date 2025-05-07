def main():
    s = input()
    ans = ''
    for i in range(len(s)):
        if s[i] == s[i].upper():
            ans += s[i]
    print(ans)

if __name__ == '__main__':
    main()