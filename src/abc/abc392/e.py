from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

def main():
    n, m = map(int, input().split())
    cables = []
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        cables.append([a, b])
    uf1 = UnionFind(n)
    for i in range(m):
        a, b = cables[i]
        uf1.unite(a, b)
    uf2 = UnionFind(n)
    rest_cables = []
    for i in range(m):
        a, b = cables[i]
        if uf1.same(a, b) and not uf2.same(a, b):
            uf2.unite(a, b)
        else:
            rest_cables.append([i+1, a, b])
    d = uf2.group_members()
    roots = set(d.keys())
    if len(roots) == 1:
        print(0)
        return
    ans = []
    for i in range(len(rest_cables)):
        root = uf2.find(rest_cables[i][1])
        for r in roots:
            if r == root:
                continue
            if not uf2.same(rest_cables[i][1], d[r][0]):
                ans.append([rest_cables[i][0], rest_cables[i][1]+1, d[r][0]+1])
                uf2.unite(rest_cables[i][1], r)
                roots.remove(r)
                break
        if len(roots) == 1:
            print(len(ans))
            for j in range(len(ans)):
                print(*ans[j])
            return

if __name__ == '__main__':
    main()