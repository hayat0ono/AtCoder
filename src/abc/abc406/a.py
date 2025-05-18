def main():
    a, b, c, d = map(int, input().split())
    if a > c:
        print('Yes')
        return
    elif a == c:
        if b > d:
            print('Yes')
            return
        else:
            print('No')
            return
    else:
        print('No')
        return

if __name__ == '__main__':
    main()