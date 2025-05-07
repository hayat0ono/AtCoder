import queue

def main():
    q = int(input())
    qu = queue.Queue()
    for _ in range(q):
        s = input()
        if s[0] == '1':
            _, x = map(int, s.split())
            qu.put(int(x))
        elif s[0] == '2':
            print(qu.get())

if __name__ == '__main__':
    main()