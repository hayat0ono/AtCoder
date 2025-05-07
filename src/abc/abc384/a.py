def main():
    n, c1, c2 = input().split()
    s = input()
    for i in range(int(n)):
        if not s[i] == c1:
            s = s[:i] + c2 + s[i+1:]
    print(s)

if __name__ == '__main__':
    main()