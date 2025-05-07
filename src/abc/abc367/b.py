def main():
    x = float(input())
    print(int(x) if x.is_integer() else x)

if __name__ == '__main__':
    main()