def main():
    h, w = map(int, input().split())
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    c = []
    for _ in range(h):
        c.append(input())
    x = input()
    for i in range(len(x)):
        if x[i] == 'L':
            if 0 <= b-1 and b-1 < w and c[a][b-1] == '.': b -= 1
        elif x[i] == 'R':
            if 0 <= b+1 and b+1 < w and c[a][b+1] == '.': b += 1
        elif x[i] == 'U':
            if 0 <= a-1 and a-1 < h and c[a-1][b] == '.': a -= 1
        elif x[i] == 'D':
            if 0 <= a+1 and a+1 < h and c[a+1][b] == '.': a += 1
    print(a+1, b+1)

if __name__ == '__main__':
    main()