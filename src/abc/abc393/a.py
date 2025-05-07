def main():
    s1, s2 = input().split()
    if s1 == 'sick':
        if s2 == 'sick':
            print('1')
        else:
            print('2')
    else:
        if s2 == 'sick':
            print('3')
        else:
            print('4')

if __name__ == '__main__':
    main()