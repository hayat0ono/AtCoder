def main():
    n, m = map(int, input().split())
    dot_dict = {}
    for _ in range(m):
        a, b = map(int, input().split())
        line_type = (a+b) % n
        if line_type not in dot_dict:
            dot_dict[line_type] = 1
        else:
            dot_dict[line_type] += 1
    ans = m*(m-1)//2
    for _, v in dot_dict.items():
        ans -= v*(v-1)//2
    print(ans)

if __name__ == '__main__':
    main()