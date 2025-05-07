def main():
    a, b = map(int, input().split())
    a, b = min(a,b), max(a,b)
    ans = set()
    ans.add(a-(b-a))
    ans.add(b+(b-a))
    if (b-a)%2 == 0:
        ans.add((a+b)/2)
    print(len(ans))

if __name__ == '__main__':
    main()