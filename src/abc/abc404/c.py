def main():
    n, m = map(int, input().split())
    graph = {}
    for i in range(n):
        graph[i] = []
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    if m != n:
        print("No")
        return
    visited = [False] * n
    now = 0
    prev = graph[now][0]
    while True:
        if visited[now]:
            break
        visited[now] = True
        if len(graph[now]) != 2:
            print("No")
            return
        next = graph[now][0] if graph[now][1] == prev else graph[now][1]
        prev = now
        now = next
    if all(visited):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()