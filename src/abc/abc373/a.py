def main():
    ans = 0
    for i in range(1, 13):
        s = input()
        if len(s) == i:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()