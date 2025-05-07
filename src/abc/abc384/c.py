def main():
    a, b, c, d, e = map(int, input().split())
    li = ['A', 'AB', 'ABC', 'ABCD', 'ABCDE', 'ABCE', 'ABD', 'ABDE', 'ABE', 'AC', 'ACD', 'ACDE', 'ACE', 'AD', 'ADE', 'AE', 'B', 'BC', 'BCD', 'BCDE', 'BCE', 'BD', 'BDE', 'BE', 'C', 'CD', 'CDE', 'CE', 'D', 'DE', 'E']
    di = {}
    for i in range(len(li)):
        score = 0
        if 'A' in li[i]:
            score += a
        if 'B' in li[i]:
            score += b
        if 'C' in li[i]:
            score += c
        if 'D' in li[i]:
            score += d
        if 'E' in li[i]:
            score += e
        if score in di:
            di[score].append(li[i])
        else:
            di[score] = [li[i]]
    for key in sorted(di.keys(), reverse=True):
        for val in di[key]:
            print(val)

if __name__ == '__main__':
    main()