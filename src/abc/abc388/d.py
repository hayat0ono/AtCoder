import bisect

def main():
    n = int(input())
    a = list(map(int, input().split()))
    diff = [0 for _ in range(n+1)]
    sum_part_of_diff = 0
    ans = [0 for _ in range(n)]
    for i in range(n):
        sum_part_of_diff += diff[i]
        added_stone = a[i] + sum_part_of_diff
        if added_stone >= (n-i-1):
            diff[i+1] += 1
        else:
            diff[i+1] += 1
            diff[i+added_stone+1] += -1
        ans[i] = max(0, added_stone - (n-(i+1)))

    print(*ans)

if __name__ == '__main__':
    main()