def main():
    n = int(input())
    d = list(map(int, input().split()))
    for i in range(n-1):
        ans = 0
        ans_list = []
        for j in range(i, n-1):
            ans += d[j]
            ans_list.append(ans)
        print(*ans_list)


if __name__ == '__main__':
    main()