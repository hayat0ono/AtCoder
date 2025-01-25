def main():
    n = int(input())
    a = list(map(int, input().split()))
    r = a[1] / a[0]
    for i in range(1, n-1):
        if a[i] * a[i] != a[i + 1] * a[i - 1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()