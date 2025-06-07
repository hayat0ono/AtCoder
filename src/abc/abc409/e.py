import sys
sys.setrecursionlimit(10**6)


def dfs(node, parent, graph, x, energy):
    for neighbor, weight in graph[node]:
        if neighbor == parent:
            continue
        diff, energy = dfs(neighbor, node, graph, x, energy)
        energy += abs(diff) * weight
        x[node] += diff
    
    return x[node], energy


def main():
    n = int(input())
    x = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    energy = 0
    _, energy = dfs(0, -1, graph, x, energy)
    print(energy)


if __name__ == '__main__':
    main()