def main():
    s = input()
    a = []
    now = 0
    for i in range(1, len(s)):
        if s[i] == '|':
            a.append(now)
            now = 0
        else:
            now += 1
    print(*a)

if __name__ == '__main__':
    main()