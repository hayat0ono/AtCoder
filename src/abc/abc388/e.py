def main():
    n = int(input())
    a = list(map(int, input().split()))
    half = n // 2
    i = 0
    j = half 
    ans = 0
    while i < half and j < n:
        if a[i] * 2 <= a[j]:
            ans += 1
            i += 1
            j += 1
        else:
            j += 1
    print(ans)

if __name__ == '__main__':
    main()