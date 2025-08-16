import bisect

def main():
    q = int(input())
    num_list = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            bisect.insort_left(num_list, query[1])
        elif query[0] == 2:
            print(num_list[0])
            num_list.pop(0)

if __name__ == '__main__':
    main()