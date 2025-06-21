def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    cell = [0 for _ in range(n)]
    ans = 0
    for i in range(q):
        ind = a[i] - 1
        if cell[ind] == 0:
            cell[ind] = 1
            if ind == 0:
                if 0 <= ind+1 < n:
                    if cell[ind+1] == 0:
                        ans += 1
                else:
                    ans += 1
            elif ind == n-1:
                if 0 <= ind-1 < n:
                    if cell[ind-1] == 0:
                        ans += 1
                else:
                    ans += 1
            elif cell[ind-1] == 0 and cell[ind+1] == 0:
                ans += 1
            elif cell[ind-1] == 1 and cell[ind+1] == 1:
                ans -= 1
        else:
            cell[ind] = 0
            if ind == 0:
                if 0 <= ind+1 < n:
                    if cell[ind+1] == 0:
                        ans -= 1
                else:
                    ans -= 1
            elif ind == n-1:
                if 0 <= ind-1 < n:
                    if cell[ind-1] == 0:
                        ans -= 1
                else:
                    ans -= 1
            elif cell[ind-1] == 1 and cell[ind+1] == 1:
                ans += 1
            elif cell[ind-1] == 0 and cell[ind+1] == 0:
                ans -= 1
        print(ans)

if __name__ == '__main__':
    main()