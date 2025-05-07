from collections import deque

def solve(h, w, k, s, start):
    ans = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(start, {start})])
    while q:
        now, visited = q.popleft()
        for dy, dx in dirs:
            next = (now[0] + dy, now[1] + dx)
            if next[0] < 0 or next[0] >= h or next[1] < 0 or next[1] >= w:
                continue
            if next in visited:
                continue
            if s[next[0]][next[1]] == '#':
                continue
            visited_tmp = visited.copy()
            visited_tmp.add(next)
            if len(visited_tmp) == k + 1:
                ans += 1
            else:
                q.append((next, visited_tmp))
    return ans

def main():
    h, w, k = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(list(input()))
    ans = 0
    for i in range(h):
        for j in range(w):
            start = (i, j)
            if s[i][j] == '.':
                ans += solve(h, w, k, s, start)
    print(ans)

if __name__ == '__main__':
    main()