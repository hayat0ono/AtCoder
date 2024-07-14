def main():
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    c1, c2 = map(int, input().split())

    if (a1-b1)*(b1-c1)+(a2-b2)*(b2-c2) == 0:
        print("Yes")
    elif (a1-b1)*(a1-c1)+(a2-b2)*(a2-c2) == 0:
        print("Yes")
    elif (b1-c1)*(a1-c1)+(b2-c2)*(a2-c2) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()