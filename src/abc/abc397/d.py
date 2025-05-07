from math import sqrt

def main():
    n = int(input())
    for d in range(1, 10**6):
        if 9*d**4-12*d*(d**3-n) < 0:
            continue
        y = (sqrt(9*d**4-12*d*(d**3-n))-3*d**2)/(6*d)
        if y > 0:
            round_y = round(y)
            if (round_y + d) ** 3 - (round_y) ** 3 == n:
                print(round_y+d, round_y)
                return
    print(-1)

if __name__ == '__main__':
    main()