import bisect

def solve(a, b, k):
    s = 0
    l = 4*10**8
    while s < l:
        mid = (s+l)//2
        start_ind = bisect.bisect_left(a, b-mid)
        end_ind = bisect.bisect_right(a, b+mid)
        num = end_ind - start_ind
        if num >= k:
            l = mid
        elif num < k:
            s = mid + 1

    start_ind = bisect.bisect_left(a, b-s)
    end_ind = bisect.bisect_right(a, b+s)
    return max(abs(a[start_ind]-b), abs(a[end_ind-1]-b))

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    for _ in range(q):
        b, k = map(int, input().split())
        ans = solve(a, b, k)
        print(ans)

if __name__ == '__main__':
    main()