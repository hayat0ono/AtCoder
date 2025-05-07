def main():
    n, t, p = map(int, input().split())
    l = list(map(int, input().split()))

    l = sorted(l, reverse=True)
    x = l[p-1]
    if x >= t:
        print(0)
        exit()
    else:
        print(t - x)
        exit()

if __name__ == '__main__':
    main()