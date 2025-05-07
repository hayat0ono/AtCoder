def sort_value(X, t):
    row_scores = [sum(sorted(row, reverse=True)[:t]) for row in X]

    sorted_indices = sorted(range(len(row_scores)), key=lambda i: row_scores[i], reverse=True)
    
    return sorted_indices

def spiral_matrix(input_list, n=6):
    matrix = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    index = 0
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = input_list[index]
            index += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = input_list[index]
            index += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = input_list[index]
                index += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = input_list[index]
                index += 1
            left += 1

    return matrix

def solve(X, t, n=6):
    sorted_X = sort_value(X, t)
    sorted_X = sorted_X[:n**2][::-1]
    res = spiral_matrix(sorted_X)

    return res

def main():
    n, m, t  = map(int, input().split())
    seed_count = 2*n*(n-1)
    X = []
    for _ in range(seed_count):
        X.append(list(map(int, input().split())))

    for l in range(t):
        res = solve(X, l+1, n)
        for i in range(n):
            print(' '.join(map(str, res[i])), flush=True)
        X = []
        for _ in range(seed_count):
            X.append(list(map(int, input().split())))

if __name__ == '__main__':
    main()