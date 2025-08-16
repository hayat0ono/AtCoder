import math

def main():
    n = int(input())
    r_max = float('-inf')
    c_max = float('-inf')
    r_min = float('inf')
    c_min = float('inf')
    for _ in range(n):
        r, c = map(int, input().split())
        r_max = max(r_max, r)
        c_max = max(c_max, c)
        r_min = min(r_min, r)
        c_min = min(c_min, c)
    print(max(math.ceil((r_max - r_min) / 2), math.ceil((c_max - c_min) / 2)))

if __name__ == '__main__':
    main()