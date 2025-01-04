def main():
    x = int(input())
    d = {}
    sum = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i*j in d:
                d[i*j] += 1
            else:
                d[i*j] = 1
            sum += i*j
    if not x in d:
        print(sum)
    else:
        print(sum - (x * d[x]))

if __name__ == '__main__':
    main()