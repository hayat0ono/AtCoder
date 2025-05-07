def add(n, reach, x, y):
    if 0 <= x < n and 0 <= y < n:
        reach.add((x, y))
    return reach

def main():
    n, m = map(int, input().split())
    ans = n * n
    reach = set()
    for _ in range(m):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        reach.add((a, b))
        reach = add(n, reach, a+2, b+1)
        reach = add(n, reach, a+1, b+2)
        reach = add(n, reach, a-1, b+2)
        reach = add(n, reach, a-2, b+1)
        reach = add(n, reach, a-2, b-1)
        reach = add(n, reach, a-1, b-2)
        reach = add(n, reach, a+1, b-2)
        reach = add(n, reach, a+2, b-1)
    print(ans - len(reach))

if __name__ == '__main__':
    main()