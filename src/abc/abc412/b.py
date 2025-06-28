def main():
    s = input()
    t = list(input())
    for i in range(1, len(s)):
        if s[i].isupper():
            if not s[i-1] in t:
                print("No")
                return
    print("Yes")
    return


if __name__ == '__main__':
    main()