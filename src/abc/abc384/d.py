def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    part_sum = 0
    part_sum_list = [0]
    for i in range(n):
        part_sum += a[i]
        part_sum_list.append(part_sum)
    part_sum_list.sort()
    if binary_search(part_sum_list, s):
        print('Yes')
        return
    part_sum = 0
    for i in range(len(a)):
        sum_tmp = s + part_sum
        if binary_search(part_sum_list, sum_tmp % sum_a):
            print('Yes')
            return
        part_sum += a[i]
    print('No')
    return

if __name__ == '__main__':
    main()