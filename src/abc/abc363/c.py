from itertools import permutations

def is_palindromic_substring(s, k):
    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        if substring == substring[::-1]:
            return True
    return False

def count_non_palindromic_permutations(S, k):
    all_permutations = set(permutations(S))
    count = 0
    
    for perm in all_permutations:
        perm_str = ''.join(perm)
        if not is_palindromic_substring(perm_str, k):
            count += 1
            
    return count

def main():
    n, k = map(int, input().split())
    S = input()
    
    result = count_non_palindromic_permutations(S, k)
    
    print(result)

if __name__ == '__main__':
    main()