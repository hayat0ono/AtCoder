def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_dict = {}
    for i in range(n):
        if a[i] in a_dict:
            a_dict[a[i]] += 1
        else:
            a_dict[a[i]] = 1
    ans = 0
    a_sub_dict = {}
    a_rest_dict = a_dict.copy()
    for i in range(n):
        if a[i] in a_sub_dict:
            a_sub_dict[a[i]] += 1
        else:
            a_sub_dict[a[i]] = 1
        a_rest_dict[a[i]] -= 1
        if a_rest_dict[a[i]] == 0:
            del a_rest_dict[a[i]]
        ans = max(ans, len(a_sub_dict) + len(a_rest_dict))
    print(ans)

if __name__ == '__main__':
    main()