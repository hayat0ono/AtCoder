def main():
    n, w = map(int, input().split())
    blocks = []
    for i in range(n):
        x, y = map(int, input().split())
        blocks.append([x, y, i+1])
    blocks.sort(key=lambda x: (x[0], x[1]))
    blocks_dict = {}
    now_x = blocks[0][0]
    now_y_num = 1
    for block in blocks:
        if now_x != block[0]:
            now_x = block[0]
            now_y_num = 1
        if now_y_num in blocks_dict:
            blocks_dict[now_y_num].append([block[1], block[2]])
        else:
            blocks_dict[now_y_num] = [[block[1], block[2]]]
        now_y_num += 1

    end_time = [float('inf') for _ in range(n)]
    diminish_time_recent = float('-inf')
    for y_num in sorted(blocks_dict):
        if len(blocks_dict[y_num]) != w:
            break
        arrival_time = max(blocks_dict[y_num], key=lambda item: item[0])[0] - 1
        diminish_time = max(arrival_time+1, diminish_time_recent+1)
        for block in blocks_dict[y_num]:
            end_time[block[1]-1] = diminish_time
        diminish_time_recent = diminish_time
    
    q = int(input())
    for _ in range(q):
        t, a = map(int, input().split())
        if end_time[a-1] > t:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()