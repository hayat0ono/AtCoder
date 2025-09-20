from collections import deque

def main():
    n = int(input())
    graph = {}
    for i in range(n):
        graph[i+1] = set()
    starts = []
    for i in range(n):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            starts.append(i+1)
        else:
            graph[a].add(i+1)
            graph[b].add(i+1)
    visited = set()
    for start in starts:
        if start in visited:
            continue
        visited.add(start)
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    print(len(visited))

if __name__ == '__main__':
    main()