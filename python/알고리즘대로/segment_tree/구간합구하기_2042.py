import math
n, m, k = map(int, input().split())
max_exp = int(math.log2(n)) + 2
segment_tree = [0] * ((2 ** max_exp) +1)
arr = [int(input()) for _ in range(n)]
arr = [0]+arr


root_idx = 1
# 트리 만들기
def mk_tree(s, e, index):
    print(s,e,index)
    if (s==e):
        segment_tree[index] = arr[s]
        return segment_tree[index]
    m = (s+e) // 2
    segment_tree[index] = mk_tree(s, m, index * 2) + mk_tree(m+1, e, (index * 2) + 1)
    return segment_tree[index]
mk_tree(1, n, 1)
print(segment_tree)

def calc_sum(target_a, target_b):
    def recursive(s, e, index):
        m = (s + e) // 2
        if (target_a <= s and e <= target_b):
            return segment_tree[index]
        if (target_b < s or e < target_a):
            return 0
        
        return recursive(s, m, index * 2) + recursive(m+1, e, (index * 2) + 1)
    return recursive(1,n,1)        

for i in range(1, 5):
    for j in range(i, 6):
        print(i,j,calc_sum(i, j))




# 트리 update로직
# 합 구하는 로직


s = 0
e = n






# arr = [0] * (2 ** 21)

# print(int(math.log2(5)) + 1)
