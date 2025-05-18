def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        next = ans * a[i]
        if next >= 10 ** k:
            ans = 1
        else:
            ans = next
    print(ans)

if __name__ == '__main__':
    main()