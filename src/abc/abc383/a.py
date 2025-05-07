def main():
    n = int(input())
    now = 0
    for i in range(n):
        t, v = map(int, input().split())
        if i == 0:
            t_past = t
        now -= (t-t_past)
        if now < 0:
            now = 0
        now += v
        t_past = t
    print(now)
        

if __name__ == '__main__':
    main()