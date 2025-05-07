def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sorted_indices_a = sorted(enumerate(a), key=lambda x: x[1], reverse=True)
    sorted_indices_b = sorted(enumerate(b), key=lambda x: x[1], reverse=True)

    indices_a = [index for index, _ in sorted_indices_a]
    indices_b = [index for index, _ in sorted_indices_b]

    ans = n

    sum_a = 0
    sum_b = 0
    for i in range(n):
        sum_a += a[indices_a[i]]
        sum_b += b[indices_a[i]]
        if sum_a > x or sum_b > y:
            ans = min(ans, i+1)
            break
    
    sum_a = 0
    sum_b = 0
    for i in range(n):
        sum_a += a[indices_b[i]]
        sum_b += b[indices_b[i]]
        if sum_a > x or sum_b > y:
            ans = min(ans, i+1)
            break
    
    print(ans)

if __name__ == '__main__':
    main()