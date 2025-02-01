def main():
    n, q = map(int, input().split())
    nest_dict = {}
    for i in range(1, n+1):
        nest_dict[i] = 1
    pos_list = [x for x in range(1, n+1)]
    ans = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            p = query[1]
            h = query[2]
            if nest_dict[h] == 1:
                ans += 1
            nest_dict[h] += 1
            if nest_dict[pos_list[p-1]] == 2:
                ans -= 1
            nest_dict[pos_list[p-1]] -= 1
            pos_list[p-1] = h
        else:
            print(ans)

if __name__ == '__main__':
    main()