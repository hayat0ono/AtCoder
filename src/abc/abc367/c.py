def check(now, k):
    if sum(now) % k == 0:
        print(*now)

def update(now, r):
    for i in range(len(now)-1, -1, -1):
        if now[i] == r[i]:
            now[i] = 1
        elif now[i] < r[i]:
            now[i] += 1
            break
    return now

def main():
    n, k = map(int, input().split())
    r = list(map(int, input().split()))
    now  = [1 for _ in range(n)]
    while now != r:
        check(now, k)
        now = update(now, r)
    check(now, k)

if __name__ == '__main__':
    main()