def main():
    n, r = map(int, input().split())
    for i in range(n):
        d, a = map(int, input().split())
        if d == 1:
            if 1600 <= r and r <= 2799:
                r += a
        if d == 2:
            if 1200 <= r and r <= 2399:
                r += a
    print(r)

if __name__ == '__main__':
    main()