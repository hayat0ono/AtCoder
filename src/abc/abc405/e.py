def prepare_factorials(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)

    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod

    inv_fact[n] = pow(fact[n], mod - 2, mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    return fact, inv_fact

def mod_combination(n, r, factorial, inv_factorial, mod):
    if r < 0 or r > n + r - 1:
        return 0
    else:
        return factorial[n + r - 1] * inv_factorial[r] % mod * inv_factorial[n - 1] % mod

def main():
    mod = 998244353
    a, b, c, d = map(int, input().split())
    ans = 0
    fact, inv_fact = prepare_factorials(max(a+b, b+c+d), mod)
    for i in range(b):
        ans += mod_combination(a, b-i, fact, inv_fact, mod) * mod_combination(i + d + 1, c, fact, inv_fact, mod)
        ans %= mod
    ans += mod_combination(b + d + 1, c, fact, inv_fact, mod)
    ans %= mod
    print(ans)

if __name__ == '__main__':
    main()