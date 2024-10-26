def main():
    S = []
    for _ in range(8):
        S.append(list(input()))
    row = [1] * 8
    col = [1] * 8
    for i in range(8):
        for j in range(8):
            if S[i][j] == '#':
                row[i] = 0
                col[j] = 0
    row = sum(row)
    col = sum(col)
    print(row*col)

if __name__ == '__main__':
    main()