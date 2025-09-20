def main():
    n, m, k = map(int, input().split())
    ans = []
    answered = [0] * (n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        answered[a] += 1
        if answered[a] == m:
            ans.append(a)
    print(*ans)

if __name__ == '__main__':
    main()