def judge(quotient):
    b = bin(quotient)[2:]
    cnt = b.count('1')
    base = len(b) - b.rfind('1') - 1
    j = (-1)**(cnt-1) * (-1)**base
    if j == 1:
        return True
    else:
        return False

def main():
    s = input()
    q = int(input())
    k = list(map(int, input().split()))
    ans = []
    for i in range(q):
        num = k[i]
        remainder = num % len(s)
        if remainder == 0:
            quotient = num // len(s)
        else:
            quotient = num // len(s) + 1
        ans_tmp = s[remainder-1]
        if judge(quotient):
            ans.append(ans_tmp)
        else:
            ans_tmp = ans_tmp.swapcase()
            ans.append(ans_tmp)
    print(*ans)

if __name__ == '__main__':
    main()