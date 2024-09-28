def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = [float('-inf'), float('-inf')]
    for i in range(n):
        ans[0] = max(ans[0], a[i])
        ans[1] = max(ans[1], b[i])
    print(ans[0] + ans[1])

if __name__ == '__main__':
    main()