def solve(h, w, s, start, goal):
    visited_flags = [[float('inf')] * w for _ in range(h)]
    visited_flags[start[0]][start[1]] = 0
    queue = [start]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    over_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (2, 0), (-2, 0), (0, 2), (0, -2)]
    ans = 0
    while True:
        visited_tmp = []
        for i, j in queue:
            visited_tmp.append((i, j))
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and visited_flags[ni][nj] == float('inf') and s[ni][nj] == '.':
                    visited_flags[ni][nj] = ans
                    queue.append((ni, nj))
        if visited_flags[goal[0]][goal[1]] != float('inf'):
            return visited_flags[goal[0]][goal[1]]
        ans += 1
        next_queue = []
        for i, j in visited_tmp:
            for di, dj in over_dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w:
                    if ans < visited_flags[ni][nj]:
                        visited_flags[ni][nj] = ans
                        next_queue.append((ni, nj))
        queue = next_queue


def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    start = (a, b)
    goal = (c, d)
    ans = solve(h, w, s, start, goal)
    print(ans)

if __name__ == '__main__':
    main()