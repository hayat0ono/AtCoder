import itertools


def floyd_warshall(adj_matrix):
    n = len(adj_matrix)
    
    distances = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            elif adj_matrix[i][j] is not None:
                distances[i][j] = adj_matrix[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    
    return distances


def bitwise_search(elements):
    n = len(elements)
    num_subsets = 1 << n
    
    for mask in range(num_subsets):
        subset = [elements[i] for i in range(n) if mask & (1 << i)]
        yield subset


def make_edges_perm(edges, perm, bits):
    edges_perm = []
    for i in range(len(perm)):
        if perm[i] in bits:
            edges_perm.append(edges[perm[i]])
        else:
            edges_perm.append((edges[perm[i]][1], edges[perm[i]][0], edges[perm[i]][2]))
    return edges_perm


def solve(edges, distances):
    ans = 0
    now = 0
    for u, v, t in edges:
        ans += distances[now][u] + t
        now = v
    ans += distances[now][-1]
    return ans


def main():
    n, m = map(int, input().split())
    edges = []
    graph = [[None for _ in range(n)] for _ in range(n)]
    for i in range(m):
        u, v, t = map(int, input().split())
        u -= 1
        v -= 1
        if graph[u][v] is None:
            graph[u][v] = t
            graph[v][u] = t
        else:
            graph[u][v] = min(graph[u][v], t)
            graph[v][u] = min(graph[v][u], t)
        edges.append((u, v, t))
    distances = floyd_warshall(graph)

    q = int(input())
    for _ in range(q):
        k = int(input())
        x = list(map(int, input().split()))
        x = [i - 1 for i in x]
        ans = float('inf')
        for perm in itertools.permutations(x):
            for bits in bitwise_search(perm):
                edges_perm = make_edges_perm(edges, perm, bits)
                ans = min(ans, solve(edges_perm, distances))
        print(ans)


if __name__ == '__main__':
    main()