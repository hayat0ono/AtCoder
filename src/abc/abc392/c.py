def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    humans = [[q[i], p[i]] for i in range(n)]
    humans.sort(key = lambda x: x[0])
    ans = []
    for i in range(n):
        ans.append(q[humans[i][1]-1])
    print(*ans)

if __name__ == '__main__':
    main()