import random


def get_minimum_cell(n, S):
    minimum_score = float('inf')
    minimum_cells = [(n, n)]
    for i in range(n):
        for j in range(n):
            if S[i][j] != '#':
                if S[i][j] < minimum_score:
                    minimum_score = S[i][j]
                    minimum_cells = [(i, j)]
                elif S[i][j] == minimum_score:
                    minimum_cells.append((i, j))

    return random.choice(minimum_cells)


def solve(n, m, S):
    s_base = [row[:] for row in S]
    for i in range(n):
        for j in range(n):
            if s_base[i][j] != '#':
                s_base[i][j] = 0

    s = [row[:] for row in S]
    for i in range(n):
        for j in range(n):
            if s[i][j] != '#':
                s[i][j] = 1 / (n**2 - m - 1)

    P = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while True:
        s_new = [row[:] for row in s_base]
        for i in range(n):
            for j in range(n):
                if s[i][j] == '#':
                    continue
                if s[i][j] == 0:
                    continue
                for dir in dirs:
                    now = (i, j)
                    while True:
                        next = (now[0] + dir[0], now[1] + dir[1])
                        if 0 <= next[0] < n and 0 <= next[1] < n:
                            if s[next[0]][next[1]] == '#':
                                s_new[now[0]][now[1]] += s[i][j] / 4
                                break
                            else:
                                now = next
                        else:
                            s_new[now[0]][now[1]] += s[i][j] / 4
                            break
        minimum_cell = get_minimum_cell(n, s_new)
        if minimum_cell == (n, n):
            break
        P.append(minimum_cell)
        s_new[minimum_cell[0]][minimum_cell[1]] = '#'
        s_base[minimum_cell[0]][minimum_cell[1]] = '#'
        s = s_new

    return P


def main():
    n, m = map(int, input().split())
    S = []
    for _ in range(n):
        s = list(input())
        S.append(s)

    P = solve(n, m, S)

    for p in P:
        print(p[0], p[1])

    # with open("outputs/0.txt", "w") as f:
    #     for p in P:
    #         print(p[0], p[1], file=f)
    

if __name__ == '__main__':
    main()