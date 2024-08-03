def main():
    n = int(input())
    a = list(map(int, input().split()))

    sorted_a = sorted(a, reverse=True)
    x = sorted_a[1]
    print(a.index(x)+1)

if __name__ == '__main__':
    main()