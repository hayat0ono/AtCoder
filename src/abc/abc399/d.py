def solve(a):
    d = {}
    ans_set = set()
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = i
        else:
            if d[a[i]] + 1 == i:
                continue
            else:
                x = d[a[i]]
                y = i
                if 0 <= x-1 < len(a) and 0 <= y-1 < len(a):
                    if a[x-1] == a[y-1]:
                        ans_set.add(tuple(sorted((a[x], a[y-1]))))
                if 0 <= x-1 < len(a) and 0 <= y+1 < len(a):
                    if a[x-1] == a[y+1]:
                        ans_set.add(tuple(sorted((a[x], a[y+1]))))
                if 0 <= x+1 < len(a) and 0 <= y-1 < len(a) and x+1 != y-1 and x+2 != y-1:
                    if a[x+1] == a[y-1]:
                        ans_set.add(tuple(sorted((a[x], a[y-1]))))
                if 0 <= x+1 < len(a) and 0 <= y+1 < len(a):
                    if a[x+1] == a[y+1]:
                        ans_set.add(tuple(sorted((a[x], a[y+1]))))
    return len(ans_set)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = solve(a)
        print(ans)

if __name__ == '__main__':
    main()