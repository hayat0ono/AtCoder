def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    fa = 0
    fb = 0
    count = 0
    for _ in range(n):
        if fb == n-1:
            print(a[-1])
            return
        
        if a[fa] <= b[fb]:
            fa += 1
            fb += 1
        elif a[fa] > b[fb] and count == 0:
            ans = a[fa]
            fa += 1
            count += 1
        else:
            print(-1)
            return
        
    print(ans)

if __name__ == '__main__':
    main()