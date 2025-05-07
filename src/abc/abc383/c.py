from collections import deque

def bfs(h, w, d, S, i, j, starts, visited):
    queue = deque(starts)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        data = queue.popleft()
        dist = data[2]
        for dir in dirs:
            x_tmp = data[0] + dir[0]
            y_tmp = data[1] + dir[1]
            if 0 <= x_tmp < h and 0 <= y_tmp < w:
                if S[x_tmp][y_tmp] == '.' and dist + 1 <= d and not visited[x_tmp][y_tmp]:
                    visited[x_tmp][y_tmp] = True
                    if dist + 1 < d:
                        queue.append([x_tmp, y_tmp, dist+1])
    return visited

def calc_ans(h, w, d, S):
    visited = [[False for _ in range(w)] for _ in range(h)]
    starts = []
    for i in range(h):
        for j in range(w):
            if S[i][j] == 'H':
                starts.append([i, j, 0])
                visited[i][j] = True
    visited = bfs(h, w, d, S, i, j, starts, visited)
    ans = sum(row.count(True) for row in visited)
    return ans

def main():
    h, w, d = map(int, input().split())
    S = []
    for _ in range(h):
        S.append(input())
    ans = calc_ans(h, w, d, S)
    print(ans)

if __name__ == '__main__':
    main()