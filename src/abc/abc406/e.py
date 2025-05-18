def prepare_factorials(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)

    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod

    inv_fact[n] = pow(fact[n], mod - 2, mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    return fact, inv_fact


def comb(n, k, fact, inv_fact, mod):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod


def solve_subproblem(i, k, cum, fact, inv_fact, mod):
    """n = 2**iの場合のテストケースに答える関数"""
    if k == 1:
        ans = 0
        for j in range(i+1):
            ans += 2**j
            ans += cum
        return ans
    else:
        if i < k:
            return 0
        ans = 0
        c = comb(i-1, k-1, fact, inv_fact, mod)
        for j in range(i):
            ans += c * 2**j
        ans += cum * comb(i, k, fact, inv_fact, mod)
        return ans
    
    
def solve(n, k, fact, inv_fact, mod):
    ans = 0
    cum = 0
    binary_n = bin(n)[2:]
    for i in range(len(binary_n)):
        if binary_n[i] == '1':
            bin_num = len(binary_n)-i-1
            ans_subproblem = solve_subproblem(bin_num, k, cum, fact, inv_fact, mod)
            ans += ans_subproblem
            ans %= mod
            cum += 2**bin_num
            cum %= mod
            k -= 1
            if k == 0:
                break
    return ans


def main():
    t = int(input())
    mod = 998244353
    fact, inv_fact = prepare_factorials(100, mod)
    for _ in range(t):
        n, k = map(int, input().split())
        ans = solve(n, k, fact, inv_fact, mod)
        print(ans)


if __name__ == '__main__':
    main()