h, w, n = map(int,input().split())
T = list(input())
S = []
for i in range(h):
    S.append(list(input()))

ans = 0

traveled_init = set()
x = 0
y = 0
traveled_init.add((x, y))
for t in T:
    if t == 'L':
        y -= 1
    elif t == 'R':
        y += 1
    elif t == 'U':
        x -= 1
    elif t == 'D':
        x += 1
    traveled_init.add((x, y))
for i in range(1, h-1):
    for j in range(1, w-1):
        if S[i][j] == '.':
            for x, y in traveled_init:
                if not ((1 <= x+i < h-1) and (1 <= y+j < w-1)):
                    FLAG = False
                    break
                if S[x+i][y+j] == '#':
                    FLAG = False
                    break
            if FLAG:
                ans += 1

print(ans)