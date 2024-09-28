def main():
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    s = input()
    for i in range(26):
        if s[i] == 'A':
            now = i
            break
    ans = 0
    for i in range(1, 26):
        for j in range(26):
            if s[j] == list[i]:
                ans += abs(now - j)
                now = j
    print(ans)

if __name__ == '__main__':
    main()