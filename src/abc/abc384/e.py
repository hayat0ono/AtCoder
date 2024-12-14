import heapq

def update_candidates(candidates, flags_visited, flags_candidated, dirs, h, w, s, x, y):
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < h and 0 <= ny < w:
            if not flags_visited[nx][ny] and not flags_candidated[nx][ny]:
                heapq.heappush(candidates, (s[nx][ny], nx, ny))
                flags_candidated[nx][ny] = True
    return candidates

def main():
    h, w, x = map(int, input().split())
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    s = []
    for _ in range(h):
        s.append(list(map(int,input().split())))
    now = s[p][q]
    candidates = []
    flags_visited = [[False] * w for _ in range(h)]
    flags_visited[p][q] = True
    flags_candidated = [[False] * w for _ in range(h)]
    flags_candidated[p][q] = True
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in dirs:
        nx, ny = p+dx, q+dy
        if 0 <= nx < h and 0 <= ny < w:
            heapq.heappush(candidates, (s[nx][ny], nx, ny))
            flags_candidated[nx][ny] = True

    while candidates:
        strength, nx, ny = candidates[0]
        if candidates[0][0] >= now / x:
            print(now)
            return
        heapq.heappop(candidates)
        now += strength
        flags_visited[nx][ny] = True
        candidates = update_candidates(candidates, flags_visited, flags_candidated,dirs, h, w, s, nx, ny)
    print(now)
    return

if __name__ == '__main__':
    main()