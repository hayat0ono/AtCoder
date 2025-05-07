def main():
    s = input()
    ans_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(s)):
        if s[i] in ans_list:
            ans_list.remove(s[i])
    print(ans_list[0])

if __name__ == '__main__':
    main()