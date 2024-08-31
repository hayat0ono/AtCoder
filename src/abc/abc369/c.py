def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_diff = []
    a_diff_group = []
    a_diff_now = float('inf')
    for i in range(1, n):
        a_diff.append(a[i] - a[i-1])
        if a_diff_now == a_diff[-1]:
            a_diff_group[-1] += 1
        else:
            a_diff_group.append(1)
            a_diff_now = a_diff[-1]
    ans = 0
    for i in range(len(a_diff_group)):
        ans += (a_diff_group[i] * (a_diff_group[i]+1) // 2)
    ans += n
    print(ans)


if __name__ == '__main__':
    main()