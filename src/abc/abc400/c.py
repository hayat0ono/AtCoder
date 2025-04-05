def max_square_root(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1

    return right

def main():
    n = int(input())
    ans = 0
    x1 = 1
    for _ in range(100):
        x1 = x1 * 2
        if x1 > n:
            break
        x2 = max_square_root(n//x1)
        ans_tmp = (x2+1)//2
        ans += ans_tmp
    print(ans)

if __name__ == '__main__':
    main()