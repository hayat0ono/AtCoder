def draw(ans, i, j, s):
    for x in range(i, j+1):
        ans[x][i] = s
        ans[x][j] = s
    for y in range(i, j+1):
        ans[i][y] = s
        ans[j][y] = s
    return ans

def main():
    n = int(input())
    ans = [['?' for _ in range(n)] for _ in range(n)]
    for i in range(1, n+1):
        j = n + 1 - i
        if i <= j:
            if i % 2 == 1:
                ans = draw(ans, i-1, j-1, '#')
            else:
                ans = draw(ans, i-1, j-1, '.')
    for i in range(n):
        print(''.join(ans[i]))

if __name__ == '__main__':
    main()