import math

def main():
    r = int(input())
    square_r = r * r
    ans = 0
    for i in range(r):
        y = i + 0.5
        points = math.floor(math.sqrt(square_r - y * y) + 0.5)
        if i == 0:
            ans += points * 2 - 1
        else:
            ans += (points * 2 - 1) * 2
    print(ans)


if __name__ == '__main__':
    main()