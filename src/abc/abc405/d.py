from collections import deque

def bfs(h, w, s, ans, d_list, queue):
    while queue:
        node, dist = queue.popleft()
        for dx, dy, arrow in [(-1, 0, 'v'), (1, 0, '^'), (0, -1, '>'), (0, 1, '<')]:
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= nx < h and 0 <= ny < w and dist + 1 < d_list[nx][ny] and s[nx][ny] != '#':
                if s[nx][ny] == '.':
                    ans[nx][ny] = arrow
                    d_list[nx][ny] = dist + 1
                queue.append(((nx, ny), dist + 1))
    return ans

def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    ans = [['' for _ in range(w)] for _ in range(h)]
    d_list = [[float('inf') for _ in range(w)] for _ in range(h)]
    queue = deque([])
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans[i][j] = '#'
            elif s[i][j] == 'E':
                ans[i][j] = 'E'
                queue.append(((i, j), 0))
                d_list[i][j] = 0
    ans = bfs(h, w, s, ans, d_list, queue)
    for i in range(h):
        print(''.join(ans[i]))

if __name__ == '__main__':
    main()