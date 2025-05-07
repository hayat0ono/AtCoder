def main():
    n = int(input())
    l = []
    min = 0
    max = 0
    for i in range(n):
        li = list(map(int, input().split()))
        l.append(li)
        min += li[0]
        max += li[1]
    
    if min > 0 or max < 0:
        print("No")
        exit()
    else:
        print("Yes")
        sum = min
        x = []
        for i in range(n):
            if sum < 0:
                if sum + (l[i][1]-l[i][0]) <= 0:
                    x.append(l[i][1])
                    sum += (l[i][1]-l[i][0])
                else:
                    x.append(l[i][0]-sum)
                    sum = 0
            else:
                x.append(l[i][0])
        print(*x)

if __name__ == '__main__':
    main()