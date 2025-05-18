def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    inc_num_prev = 0
    inc_num = 0
    prev = p[0]
    for i in range(1, n):
        if p[i] > prev:
            inc_num += 1
        elif inc_num != 0:
            if inc_num_prev != 0:
                ans += inc_num_prev * inc_num
            inc_num_prev = inc_num
            inc_num = 0
        prev = p[i]
    if inc_num != 0:
        ans += inc_num_prev * inc_num
    print(ans)

if __name__ == '__main__':
    main()