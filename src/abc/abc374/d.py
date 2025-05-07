import itertools
import math

def solve(perm, bit_i, list):
    ans = 0
    now = [0, 0]
    for i in range(len(perm)):
        a, b, c, d = list[perm[i]]
        if bit_i[i] == '1':
            ans += math.sqrt((now[0] - a)**2 + (now[1] - b)**2)
            now[0] = c
            now[1] = d
        else:
            ans += math.sqrt((now[0] - c)**2 + (now[1] - d)**2)
            now[0] = a
            now[1] = b
    return ans

def main():
    n, s, t = map(int, input().split())
    list = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        list.append([a, b, c, d])
    len_s = float('inf')
    for perm in itertools.permutations(range(n)):
        for i in range(2**n):
            bit_i = bin(i)[2:].zfill(n)
            tmp = solve(perm, bit_i, list)
            len_s = min(len_s, tmp)
    len_t = 0
    for i in range(n):
        a, b, c, d = list[i]
        len_t += math.sqrt((a-c)**2 + (b-d)**2)
    print(len_s / s + len_t / t)

if __name__ == '__main__':
    main()