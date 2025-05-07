def main():
    a = list(map(int, input().split()))
    if a == [2, 1, 3, 4, 5]:
        print('Yes')
        return
    if a == [1, 3, 2, 4, 5]:
        print('Yes')
        return
    if a == [1, 2, 4, 3, 5]:
        print('Yes')
        return
    if a == [1, 2, 3, 5, 4]:
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()