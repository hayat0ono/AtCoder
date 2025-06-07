def main():
    n, l = map(int, input().split())
    d = list(map(int, input().split()))
    if l % 3 != 0:
        print(0)
        return
    
    point_dict = {}
    now = 0
    point_dict[now] = 1
    for i in range(n - 1):
        now = (now + d[i]) % l
        if now in point_dict:
            point_dict[now] += 1
        else:
            point_dict[now] = 1
    ans = 0
    for k in point_dict.keys():
        if (k + l // 3) % l in point_dict and (k + 2 * l // 3) % l in point_dict:
            ans += point_dict[k] * point_dict[(k + l // 3) % l] * point_dict[(k + 2 * l // 3) % l]
    print(ans // 3)


if __name__ == '__main__':
    main()