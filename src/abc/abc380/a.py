def main():
    n = input()
    num_1 = 0
    num_2 = 0
    num_3 = 0
    for i in range(len(n)):
        if n[i] == '1':
            num_1 += 1
        elif n[i] == '2':
            num_2 += 1
        elif n[i] == '3':
            num_3 += 1
    if num_1 == 1 and num_2 == 2 and num_3 == 3:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()