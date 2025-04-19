import bisect

def main():
    n, m = map(int, input().split())
    cooking_dict = {}
    for i in range(1, m+1):
        s = list(map(int,input().split()))
        s = s[1:]
        cooking_dict[i] = s
    b = list(map(int,input().split()))
    edible_food_to_date = {}
    for i in range(1, n+1):
        edible_food_to_date[b[i-1]] = i
    edible_dates = []
    for i in range(1, m+1):
        s = cooking_dict[i]
        edible_date = 0
        for j in range(len(s)):
            edible_date = max(edible_date, edible_food_to_date[s[j]])
        edible_dates.append(edible_date)
    edible_dates.sort()
    for i in range(1, n+1):
        ans = bisect.bisect_right(edible_dates, i)
        print(ans)

if __name__ == '__main__':
    main()