def judge(S, T, m, i, j):
    for a in range(m):
        for b in range(m):
            if S[i+a][j+b] != T[a][b]:
                return False
    return True

def main():
    n, m = map(int, input().split())
    S = []
    T = []
    for i in range(n):
        S.append(list(input()))
    for i in range(m):
        T.append(list(input()))
    for i in range(n):
        if i + m > n:
            break
        for j in range(n):
            if j + m > n:
                break
            if judge(S, T, m, i, j):
                print(i+1, j+1)
                return
                        
if __name__ == '__main__':
    main()