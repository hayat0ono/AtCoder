import bisect

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        index_left = bisect.bisect_left(a, 2*a[i])
        ans += n - index_left
    print(ans)

if __name__ == '__main__':
    main()