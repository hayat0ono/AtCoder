def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    num_list = [False] * (m + 1)
    num_list[0] = True
    for i in range(n):
        if not num_list[a[i]]:
            num_list[a[i]] = True
            if all(num_list):
                print(n - i)
                return
    print(0)
    return

if __name__ == '__main__':
    main()