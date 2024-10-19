import bisect

def solve(n, k, a, b):
    li = [a, b]
    li = list(zip(*li))
    li.sort(key=lambda x: x[0])
    li = list(zip(*li))
    a, b = li
    a = list(a)
    b = list(b)
    b_part = b[0:k-1]
    b_part.sort()
    sum_b = sum(b_part)
    ans = float('inf')
    for i in range(k-1, n):
        ans = min(ans, a[i]*(sum_b+b[i]))
        insection = bisect.bisect_left(b_part, b[i])
        if insection != k-1:
            b_part.insert(insection, b[i])
            sum_b += b[i] - b_part.pop(-1)
    return ans

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ans = solve(n, k, a, b)
        print(ans)

if __name__ == '__main__':
    main()