def main():
    n = int(input())
    date = []
    for _ in range(n):
        date.append(list(map(int, input().split())))
    q = int(input())
    for _ in range(q):
        t, d = map(int, input().split())
        q = date[t-1][0]
        r = date[t-1][1]
        if d % q == r:
            print(d)
        elif d % q < r:
            print((d-(d%q))+r)
        else:
            print((d-(d%q))+r+q)

if __name__ == '__main__':
    main()