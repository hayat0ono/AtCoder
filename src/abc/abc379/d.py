from collections import defaultdict
import bisect

def main():
    q = int(input())
    li = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            li.insert(0, 0)
        elif query[0] == 2:
            li = [x + query[1] for x in li]
        else:
            ins = bisect.bisect_left(li, query[1])
            print(len(li) - ins)
            li = li[:ins]

if __name__ == '__main__':
    main()