def main():
    a, b, c = map(int, input().split())
    if a == b:
        print("Yes")
        return
    elif a == c:
        print("Yes")
        return
    elif b == c:
        print("Yes")
        return
    else:
        print("No")

if __name__ == '__main__':
    main()