def main():
    d = input()

    if d == 'N':
        print('S')
    if d == 'S':
        print('N')
    if d == 'E':
        print('W')
    if d == 'W':
        print('E')

    if d == 'NE':
        print('SW')
    if d == 'SW':
        print('NE')
    if d == 'NW':
        print('SE')
    if d == 'SE':
        print('NW')

if __name__ == '__main__':
    main()