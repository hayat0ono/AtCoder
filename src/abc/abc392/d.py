def calc_probability(dict_a, dict_b):
    ans = 0
    for k in dict_a.keys():
        if k in dict_b:
            ans += dict_a[k] * dict_b[k]
    return ans

def main():
    n = int(input())
    dicts = []
    for _ in range(n):
        s = list(map(int, input().split()))
        d = {}
        for i in range(1, len(s)):
            if s[i] in d:
                d[s[i]] += 1 / s[0]
            else:
                d[s[i]] = 1 / s[0]
        dicts.append(d)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                ans = max(ans, calc_probability(dicts[i], dicts[j]))
    print(ans)

if __name__ == '__main__':
    main()