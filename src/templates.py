# inputs
'''
# abcde => 'abcde'
s = input()

# abcde = ['a','b','c','d','e']
s = list(input())

# 5 => 5
a = int(input())

# 1 2 => 1, 2
x,y = map(int,input().split())

# 1 2 3 4 5 ... n => ['1','2','3','4','5',...,'n']
li = input().split()

# 1 2 3 4 5 ... n => [1,2,3,4,5,...,n]
li = list(map(int,input().split()))

# FFFTFTTFF => ['FFF', 'F', '', 'FF']
li = input().split('T')
'''

# binary search
'''
import bisect

# examples
a=[1,3,5,7,9,11,13,15,17,19]
x=4
insert_index = bisect.bisect_left(a,x)
# insert_index=2
a.insert(insert_index,x)
# a = [1,3,4,5,7,9,11,13,15,17,19]
bisect.insort_left(a, x)
# a = [1,3,4,5,7,9,11,13,15,17,19] 左側に挿入
bisect.insort_right(a,x)
# a = [1,3,4,5,7,9,11,13,15,17,19] 右側に挿入
'''

# Segment Tree
'''
# make function you want to implement in segment tree
def segfunc(x, y):
    return 

# define identity element
ide_ele =

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1
            
        def add(self, k, x):
        """
        k番目の値にxを加算
        k: index(0-index)
        x: 加算する値
        """
        k += self.num
        self.tree[k] += x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def multiple(self, k, x):
        """
        k番目の値にxを乗算
        k: index(0-index)
        x: 乗算する値
        """
        k += self.num
        self.tree[k] *= x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

'''

# sieve of eratosthenes
# n以下の素数を列挙
'''
def sieve_of_eratosthenes(n):
    prime_flags = [True] * (n + 1)
    
    prime_flags[0] = prime_flags[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if prime_flags[i]:
            for j in range(i*i, n+1, i):
                prime_flags[j] = False
    
    primes = [i for i in range(2, n+1) if prime_flags[i]]
    
    return primes
'''