def calc_ans_tmp(h, w, d, S, i, j):
    x_1, y_1 = i//w, i%w
    x_2, y_2 = j//w, j%w
    ans = 0
    for i in range(h):
        for j in range(w):
            if ((abs(x_1 - i) + abs(y_1 - j)) <= d or (abs(x_2 - i) + abs(y_2 - j)) <= d) and S[i][j] == '.':
                ans += 1
    return ans

def main():
    h, w, d = map(int, input().split())
    S = []
    for _ in range(h):
        S.append(input())
    ans = float('-inf')
    for i in range(h*w):
        for j in range(h*w):
            if S[i//w][i%w] == '.' and S[j//w][j%w] == '.':
                ans = max(ans, calc_ans_tmp(h, w, d, S, i, j))
    print(ans)

if __name__ == '__main__':
    main()