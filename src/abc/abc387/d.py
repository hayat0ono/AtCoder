from collections import deque

def dfs(h, w, grid):
    visited_v = [[False] * w for _ in range(h)]
    visited_h = [[False] * w for _ in range(h)]
    for i in range(w):
        for j in range(h):
            if grid[j][i] == 'S':
                start = (i, j)
                visited_v[j][i] = True
                visited_h[j][i] = True
            if grid[j][i] == 'G':
                goal = (i, j)
    v_dirs = [(0, 1), (0, -1)]
    h_dirs = [(1, 0), (-1, 0)]
    queue_v = deque([[start[0], start[1], 1, 0]])
    queue_h = deque([[start[0], start[1], -1, 0]])
    ans = float('inf')
    while queue_v:
        x, y, f, d = queue_v.popleft()
        if (x, y) == goal:
            ans = min(ans, d)
        if f == 1:
            dirs = v_dirs
        else:
            dirs = h_dirs
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not visited_v[ny][nx] and grid[ny][nx] != '#':
                visited_v[ny][nx] = True
                queue_v.append([nx, ny, (-1)*f, d+1])
    while queue_h:
        x, y, f, d = queue_h.popleft()
        if (x, y) == goal:
            ans = min(ans, d)
        if f == 1:
            dirs = v_dirs
        else:
            dirs = h_dirs
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not visited_h[ny][nx] and grid[ny][nx] != '#':
                visited_h[ny][nx] = True
                queue_h.append([nx, ny, (-1)*f, d+1])
    if ans == float('inf'):
        return -1
    return ans

def main():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())
    ans = dfs(h, w, grid)
    print(ans)
    
if __name__ == '__main__':
    main()