class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n+1)

    def update(self, idx, val):
        while idx <= self.n:
            self.data[idx] += val
            idx += idx & -idx

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.data[idx]
            idx -= idx & -idx
        return s

    def find(self, target):
        idx = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask > 0:
            next_idx = idx + bit_mask
            if next_idx <= self.n and self.data[next_idx] < target:
                target -= self.data[next_idx]
                idx = next_idx
            bit_mask >>= 1
        return idx + 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = [0 for _ in range(n)]
    bit = BIT(n)
    for i in range(n):
        bit.update(i+1, 1)
    for i in range(n, 0, -1):
        pos = bit.find(p[i-1])
        ans[pos-1] = i
        bit.update(pos, -1)
    print(*ans)

if __name__ == '__main__':
    main()