def main():
    h, w, n = map(int, input().split())
    x_dict = {}
    for i in range(h):
        x_dict[i] = set()
    y_dict = {}
    for i in range(w):
        y_dict[i] = set()
    for i in range(n):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        x_dict[x].add(y)
        y_dict[y].add(x)
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        k -= 1
        if n == 1:
            print(len(x_dict[k]))
            for y in x_dict[k]:
                y_dict[y].discard(k)
            x_dict[k].clear()
        elif n == 2:
            print(len(y_dict[k]))
            for x in y_dict[k]:
                x_dict[x].discard(k)
            y_dict[k].clear()

if __name__ == '__main__':
    main()