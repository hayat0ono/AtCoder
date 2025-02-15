def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(1, len(s)):
            if not 0 <= i + 2 * j < len(s):
                break
            if s[i] == 'A' and s[i + j] == 'B' and s[i + 2 * j] == 'C':
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()