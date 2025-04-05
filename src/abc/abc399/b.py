def main():
    n = int(input())
    p = list(map(int, input().split()))
    score_dict = {}
    for i in range(n):
        if p[i] not in score_dict:
            score_dict[p[i]] = []
        score_dict[p[i]].append(i)
    ans = [0 for _ in range(n)]
    r = 1
    for score in sorted(score_dict.keys(), reverse=True):
        for i in score_dict[score]:
            ans[i] = r
        r += len(score_dict[score])
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()