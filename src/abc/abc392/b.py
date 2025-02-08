def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans_list = [1 for _ in range(n)]
    for i in range(m):
        ans_list[a[i]-1] = 0
    ans = []
    for i in range(n):
        if ans_list[i] == 1:
            ans.append(i+1)
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()