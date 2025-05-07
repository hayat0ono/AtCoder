def main():
    n = int(input())
    s = [input()]
    for i in range(1, n-1):
        S = input()
        if S == 'sweet' and s[-1] == 'sweet':
            print('No')
            exit()
        s.append(S)
    print('Yes')

if __name__ == '__main__':
    main()