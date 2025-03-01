def main():
    n, q = map(int, input().split())
    pig_pos = [i for i in range(1, n+1)]
    pos_to_label = {i: i for i in range(1, n+1)}
    label_to_pos = {i: i for i in range(1, n+1)}
    for _ in range(q):
        op = list(map(int, input().split()))
        if op[0] == 1:
            a, b = op[1], op[2]
            pig_pos[a-1] = label_to_pos[b]
        elif op[0] == 2:
            a, b = op[1], op[2]
            a_pos = label_to_pos[a]
            b_pos = label_to_pos[b]
            pos_to_label[a_pos] = b
            pos_to_label[b_pos] = a
            label_to_pos[a] = b_pos
            label_to_pos[b] = a_pos
        elif op[0] == 3:
            a = op[1]
            print(pos_to_label[pig_pos[a-1]])

if __name__ == '__main__':
    main()