import itertools


def solve(n, m, c, animal_dict, digits):
    animal_count = [0] * m
    ans = 0
    for i in range(n):
        if digits[i] == '1':
            ans += c[i]
            for j in animal_dict[i]:
                animal_count[j] += 1
        elif digits[i] == '2':
            ans += 2 * c[i]
            for j in animal_dict[i]:
                animal_count[j] += 2
    if all(x >= 2 for x in animal_count):
        return ans
    else:
        return float('inf')


def main():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    animal_dict = {}
    for i in range(n):
        animal_dict[i] = []
    for i in range(m):
         animal_info = list(map(int, input().split()))
         for j in range(1, len(animal_info)):
             animal_dict[animal_info[j]-1].append(i)
    ans = float('inf')
    for digits in itertools.product('012', repeat=n):
        ans = min(ans, solve(n, m, c, animal_dict, digits))
    print(ans)


if __name__ == '__main__':
    main()