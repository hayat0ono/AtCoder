import bisect

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n+1):
        ind = bisect.bisect_left(a, i)
        num = n - ind
        if num >= i:
            ans = i
    print(ans)

if __name__ == '__main__':
    main()