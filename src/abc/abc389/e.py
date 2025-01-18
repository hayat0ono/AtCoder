import math

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    sum_1_over_pi = 0
    for i in range(n):
        sum_1_over_pi += 1 / p[i]
    ans = 0
    dict_ki = {}
    sum_price = 0
    list_add_price = []
    for i in range(n):
        dict_ki[i] = math.floor(math.sqrt(m / sum_1_over_pi) / p[i])
        ans += dict_ki[i]
        sum_price += dict_ki[i] ** 2 * p[i]
        list_add_price.append((dict_ki[i] * 2 + 1) * p[i])
    list_add_price.sort()
    for i in range(n):
        sum_price += list_add_price[i]
        if sum_price > m:
            print(ans)
            return
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()