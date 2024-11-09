def main():
    n, k = map(int, input().split())
    s = input()
    seq = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == "O":
            seq += 1
            if seq == k:
                ans += 1
                seq = 0
        elif s[i] == "X":
            seq = 0
    print(ans)

if __name__ == '__main__':
    main()