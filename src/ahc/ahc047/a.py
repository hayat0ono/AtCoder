import numpy as np


def reform_str_dict(str_dict):
    new_str_dict = str_dict.copy()
    for s in str_dict:
        for S in str_dict:
            if s in S:
                new_str_dict[S] += str_dict[s]
            if S in s:
                new_str_dict[s] += str_dict[S]
    return new_str_dict


def resample_probability(p, total=88):
    p = np.array(p)
    p = p.astype(np.float64)
    p /= sum(p)
    ans = np.random.multinomial(total, p)
    ans += (100 - total) // len(p)
    ans = ans.tolist()
    return ans


def calc_initial_probability(str_dict):
    ans = {}
    str_to_num = {'a': [0, 1], 'b': [2, 3], 'c': [4, 5], 'd': [6, 7], 'e': [8, 9], 'f': [10, 11]}
    strs = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'f']
    for i in range(len(strs)):
        ans[i] = {}
        ans[i]['str'] = strs[i]
        ans[i]['probability'] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    keys = sorted(str_dict, key=str_dict.get, reverse=True)[:2]
    for i in range(len(keys)):
        s = keys[i]
        past = s[0]
        for st in str_to_num:
            ans[str_to_num[st][1-i]]['probability'][str_to_num[past][i]] += 10
        for j in range(1, len(s)):
            now = s[j]
            ans[str_to_num[past][i]]['probability'][str_to_num[now][i]] += 100
            past = now
    for i in ans:
        probability = ans[i]['probability']
        probability = resample_probability(probability, 100)
        ans[i]['probability'] = probability

    return ans


def generate_ans(ans):
    new_ans = {}
    for i in ans:
        new_ans[i] = {}
        new_ans[i]['str'] = ans[i]['str']
        probability = ans[i]['probability']
        new_probability = resample_probability(probability)
        new_ans[i]['probability'] = new_probability

    return new_ans
    

def calc_probability(ans, vn, s):
    str_to_num = {'a': [0, 1], 'b': [2, 3], 'c': [4, 5], 'd': [6, 7], 'e': [8, 9], 'f': [10, 11]}

    dict_now = {}
    for i in str_to_num[s[0]]:
        dict_now[i] = vn[i]
    for i in range(1, len(s)):
        dict_next = {}
        for j in str_to_num[s[i]]:
            prob_tmp = 0
            for k in dict_now:
                prob_tmp += ans[k]['probability'][j] * dict_now[k]
            dict_next[j] = prob_tmp
        dict_now = dict_next
    prob = 0
    for i in dict_now:
        prob += dict_now[i]
    return prob


def ans_to_score(ans, str_dict):
    score = 0

    p = []
    for i in ans:
        p.append(ans[i]['probability'])
    p = np.array(p)
    p = p.astype(np.float64)
    p /= 100
    pn = np.linalg.matrix_power(p, 100)
    v0 = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    vn = np.dot(v0, pn)
    vn *= 100

    for s in str_dict:
        score += str_dict[s] * calc_probability(ans, vn, s)
    return score


def solver(ans, score, str_dict, T, cooldown=0.9):
    new_ans = generate_ans(ans)
    new_score = ans_to_score(new_ans, str_dict)
    if new_score > score:
        ans = new_ans
        score = new_score
    else:
        if np.random.rand() < np.exp(10000 * (new_score - score) / T):
            ans = new_ans
            score = new_score
    
    T = T * cooldown
    return ans, score, T


def main():
    n, m, l = map(int, input().split())
    str_dict = {}
    for _ in range(n):
        s, t = input().split()
        str_dict[s] = int(t)
    str_dict = reform_str_dict(str_dict)

    ans = calc_initial_probability(str_dict)

    score = ans_to_score(ans, str_dict)
    itr_max = 100
    T = 100
    T_min = 1
    for _ in range(itr_max):
        ans, score, T = solver(ans, score, str_dict, T)
        if T < T_min:
            break

    for i in range(m):
        ans_dict = ans[i]
        print(ans_dict['str'], *ans_dict['probability'], sep=' ')


if __name__ == '__main__':
    main()