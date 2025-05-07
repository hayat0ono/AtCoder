def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    min_h = float('inf')
    max_h = float('-inf')
    min_w = float('inf')
    max_w = float('-inf')
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                min_h = min(min_h, i)
                max_h = max(max_h, i)
                min_w = min(min_w, j)
                max_w = max(max_w, j)
    for i in range(min_h, max_h+1):
        for j in range(min_w, max_w+1):
            if s[i][j] == '.':
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()