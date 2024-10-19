from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        distance = {start: 0}
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor not in distance:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
                elif neighbor == start:
                    return distance[node] + 1
        
        return -1

def main():
    n, m = map(int, input().split())
    g = Graph()
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g.add_edge(a, b)
    ans = g.bfs(0)
    print(ans)

if __name__ == '__main__':
    main()