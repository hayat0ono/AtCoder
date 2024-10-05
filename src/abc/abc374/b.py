def main():
    s = input()
    t = input()
    lens = len(s)
    lent = len(t)
    l = min(len(s), len(t))
    for i in range(l):
        if s[i] != t[i]:
            print(i + 1)
            return
    if l == lens and l == lent:
        print(0)
        return
    else:
        print(l + 1)
        return

if __name__ == '__main__':
    main()