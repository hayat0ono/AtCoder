def calc_max(a, m):
    sum = 0
    for i in range(len(a)):
        if sum + a[i]*(len(a)-i) > m:
            return i-1
        sum += a[i]
    return -2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    max = calc_max(a, m)
    if max == -1:
        print(m//n)
        return
    if max == -2:
        print('infinite')
        return
    
    sum = 0
    for i in range(max+1):
        sum += a[i]
    rest = m - sum - a[max]*(n-max-1)
    print(a[max] + rest//(n-max-1))
    return

if __name__ == '__main__':
    main()