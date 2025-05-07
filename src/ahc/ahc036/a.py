from collections import deque


def bfs_shortest_path(graph, start, goal):
    if start == goal:
        return [start]

    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None


def make_list_a(n, m, t, la, lb, graph, t_list):
    a = [0] * la
    for i in range(n):
        a[i] = i
    return a


def solve(n, m, t, la, lb, graph, t_list):
    now = 0
    for i in range(t):
        path = bfs_shortest_path(graph, now, t_list[i])
        for j in range(1, len(path)):
            print(f's 1 {path[j]} 0')
            print(f'm {path[j]}')
        now = t_list[i]


def main():
    n, m, t, la, lb = map(int, input().split())
    graph = {}
    for i in range(n):
        graph[i] = []
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    t_list = list(map(int, input().split()))
    cities = []
    for _ in range(n):
        x, y = map(int, input().split())
        cities.append([x, y])

    a = make_list_a(n, m, t, la, lb, graph, t_list)
    print(*a)

    solve(n, m, t, la, lb, graph, t_list)


if __name__ == '__main__':
    main()