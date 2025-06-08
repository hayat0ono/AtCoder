from typing import Dict, List, Tuple

Color = Tuple[float, float, float]
State = Tuple[Color, int]
Operation = Tuple[int, int, int] | Tuple[int, int, int, int] | Tuple[int, int, int, int, int]


N, K, H, T, D = map(int, input().split())
Colors = [tuple(map(float, input().split())) for _ in range(K)]
Target_Colors = [tuple(map(float, input().split())) for _ in range(H)]


def make_txt_file(ver_wall: List[List[int]], hor_wall: List[List[int]], ops: List[Operation]):
    with open("outputs/4.txt", "w") as f:
        for row in ver_wall:
            print(" ".join(map(str, row)), file=f)
        for row in hor_wall:
            print(" ".join(map(str, row)), file=f)
        for op in ops:
            print(" ".join(map(str, op)), file=f)


def print_ans(ver_wall: List[List[int]], hor_wall: List[List[int]], ops: List[Operation]):
    for i in range(N):
        print(*ver_wall[i])
    for i in range(N-1):
        print(*hor_wall[i])
    for op in ops:
        print(*op)


def color_distance(c1: Color, c2: Color) -> float:
    return sum((a - b) ** 2 for a, b in zip(c1, c2))


def mix_colors(colors: List[Tuple[Color, float]]) -> Color:
    total = sum(w for _, w in colors)
    if total == 0:
        return (0.0, 0.0, 0.0)
    c = sum(w * col[0] for col, w in colors) / total
    m = sum(w * col[1] for col, w in colors) / total
    y = sum(w * col[2] for col, w in colors) / total
    return (c, m, y)


def get_paired_colors(colors: List[Color]) -> List[Tuple[Color, Tuple[int, int]]]:
    paired_colors = []
    for i in range(K):
        for j in range(i+1, K):
            paired_colors.append((mix_colors([(colors[i], 1), (colors[j], 1)]), (i, j)))
    return paired_colors


def get_nearest_color_and_score(target_colors: List[Color], colors: List[Color]) -> List[Tuple[int, float]]:
    nearest_colors_and_score = []
    for i in range(H):
        score = float('inf')
        for j in range(K):
            if score > 10**4 * color_distance(colors[j], target_colors[i]):
                score = 10**4 * color_distance(colors[j], target_colors[i])
                color_idx = j
        nearest_colors_and_score.append((color_idx, score))
    return nearest_colors_and_score


def get_nearest_color(target_colors: List[Color], colors: List[Color]) -> List[Tuple[int, float]]:
    nearest_colors = []
    for i in range(H):
        score = float('inf')
        for j in range(K):
            if score > 10**4 * color_distance(colors[j], target_colors[i]):
                score = 10**4 * color_distance(colors[j], target_colors[i])
                color_idx = j
        nearest_colors.append((color_idx, score))
    return nearest_colors


def get_nearest_color_pair_and_score(target_colors: List[Color], colors_pair: List[Tuple[Color, Tuple[int, int]]]) -> List[Tuple[Tuple[int, int], float]]:
    nearest_color_pair_and_score = []
    for i in range(H):
        score = float('inf')
        for j in range(len(colors_pair)):
            if score > 10**4 * color_distance(colors_pair[j][0], target_colors[i]):
                score = 10**4 * color_distance(colors_pair[j][0], target_colors[i])
                color_pair_idx = colors_pair[j][1]
        nearest_color_pair_and_score.append((color_pair_idx, score))
    return nearest_color_pair_and_score


def main():
    ver_wall = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    ]

    hor_wall = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    Color_index_to_pallete = {}
    for i in range(K):
        Color_index_to_pallete[i] = (0, i)
    representive_indices = []
    for i in range(1, N):
        for j in range(N):
            if j % 2 == 0:
                representive_indices.append((i, j))
    for i in range(K):
        for j in range(i+1, K):
            Color_index_to_pallete[(i, j)] = (representive_indices.pop(0), False)

    paired_colors = get_paired_colors(Colors)
    nearest_color_and_score = get_nearest_color_and_score(Target_Colors, Colors)
    nearest_color_pair_and_score = get_nearest_color_pair_and_score(Target_Colors, paired_colors)

    res_dict = {}
    for i in range(H):
        if nearest_color_and_score[i][1] > nearest_color_pair_and_score[i][1]:
            indices = nearest_color_pair_and_score[i][0]
            if indices in res_dict:
                res_dict[indices] += 1
            else:
                res_dict[indices] = 1
    
    raw_ops = [[] for _ in range(H)]
    for i in range(H):
        if nearest_color_and_score[i][1] <= nearest_color_pair_and_score[i][1]:
            idx = nearest_color_and_score[i][0]
            raw_ops[i].append((1, Color_index_to_pallete[idx][0], Color_index_to_pallete[idx][1], idx))
            raw_ops[i].append((2, Color_index_to_pallete[idx][0], Color_index_to_pallete[idx][1]))
        elif Color_index_to_pallete[nearest_color_pair_and_score[i][0]][1]:
            indices = nearest_color_pair_and_score[i][0]
            raw_ops[i].append((2, Color_index_to_pallete[indices][0][0], Color_index_to_pallete[indices][0][1]))
            Color_index_to_pallete[indices] = (Color_index_to_pallete[indices][0], False)
            res_dict[indices] -= 1
        elif res_dict[nearest_color_pair_and_score[i][0]] != 1:
            indices = nearest_color_pair_and_score[i][0]
            raw_ops[i].append((1, Color_index_to_pallete[indices][0][0], Color_index_to_pallete[indices][0][1], indices[0]))
            raw_ops[i].append((1, Color_index_to_pallete[indices][0][0], Color_index_to_pallete[indices][0][1], indices[1]))
            raw_ops[i].append((2, Color_index_to_pallete[indices][0][0], Color_index_to_pallete[indices][0][1]))
            Color_index_to_pallete[indices] = (Color_index_to_pallete[indices][0], True)
            res_dict[indices] -= 1
        else:
            if nearest_color_and_score[i][1] > nearest_color_pair_and_score[i][1] + D:
                indices = nearest_color_pair_and_score[i][0]
                raw_ops[i].append((1, Color_index_to_pallete[indices][0][0], Color_index_to_pallete[indices][0][1], indices[0]))
                raw_ops[i].append((1, Color_index_to_pallete[indices][0][0], Color_index_to_pallete[indices][0][1], indices[1]))
                raw_ops[i].append((2, Color_index_to_pallete[indices][0][0], Color_index_to_pallete[indices][0][1]))
                Color_index_to_pallete[indices] = (Color_index_to_pallete[indices][0], True)
            else:
                idx = nearest_color_and_score[i][0]
                raw_ops[i].append((1, Color_index_to_pallete[idx][0], Color_index_to_pallete[idx][1], idx))
                raw_ops[i].append((2, Color_index_to_pallete[idx][0], Color_index_to_pallete[idx][1]))

    ops = []
    for i in range(H):
        for j in range(len(raw_ops[i])):
            ops.append(raw_ops[i][j])

    print_ans(ver_wall, hor_wall, ops)


if __name__ == '__main__':
    main()