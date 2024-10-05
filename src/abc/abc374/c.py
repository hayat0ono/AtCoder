def main():
    n = int(input())
    k = list(map(int, input().split()))
    s = sum(k)
    ans = float('inf')
    for i in range(2**n):
        tmp = 0
        bit_i = bin(i)[2:].zfill(n)
        for j in range(n):
            if bit_i[j] == '1':
                tmp += k[j]
        tmp_ans = max(tmp, s - tmp)
        ans = min(ans, tmp_ans)
    print(ans)    

if __name__ == '__main__':
    main()