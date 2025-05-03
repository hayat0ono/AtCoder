from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()
        if node == goal:
            return dist
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))


def solve(li):
    graph = {}
    for i in range(len(li)):
        graph[i] = []
    for i in range(len(li)):
        for j in range(1, li[i]+1):
            if i+j < len(li):
                graph[i].append(i+j)
    ans = bfs(graph, 0, len(li)-1)
    return ans


def main():
    n = int(input())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c.reverse()
    a.reverse()
    c.append(0)
    a.append(1)
    ans = 0
    start = float('-inf')
    for i in range(n):
        if a[i] == 1:
            if start == float('-inf'):
                start = i
            else:
                ans += solve(c[start: i+1])
                start = i
    print(ans)

if __name__ == '__main__':
    main()