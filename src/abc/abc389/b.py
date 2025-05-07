def main():
    x = int(input())
    n = 1
    while True:
        if x == 1:
            print(n)
            break
        n += 1
        x = x // n

if __name__ == '__main__':
    main()