def main():
    a, b, c = map(int, input().split())
    if b < c:
        print('Yes' if a < b or c < a else 'No')
    else:
        print('Yes' if c < a and a < b else 'No')

if __name__ == '__main__':
    main()