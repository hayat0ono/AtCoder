def main():
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for key in d.keys():
        if d[key] > 1:
            if d[key] == 4:
                print(2)
                return
            else:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()