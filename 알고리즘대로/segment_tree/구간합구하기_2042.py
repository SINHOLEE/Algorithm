import math
def solution(n,m,k):
    arr = [int(input()) for _ in range(n)]
    max_exp = int(math.log2(n)) + 2
    segment_tree = [0] * ((2 ** max_exp) +1)
    arr = [0]+arr
    root_idx = 1
    
    def update(added_index,added_num):
        def add(index,s,e):
            if s==e:
                temp = segment_tree[index]
                segment_tree[index] = added_num
                return added_num - temp
            m = (s+e)//2
            if s<=added_index<=m:
                target = add(index*2, s,m)
            else:
                target = add(index*2+1, m+1,e)
            segment_tree[index]+= target
            return target
        add(1,1,n)
        

    def mk_tree(s, e, index):
        if (s==e):
            segment_tree[index] = arr[s]
            return segment_tree[index]
        m = (s+e) // 2
        segment_tree[index] = mk_tree(s, m, index * 2) + mk_tree(m+1, e, (index * 2) + 1)
        return segment_tree[index]


    def calc_sum(target_a, target_b):
        def recursive(s, e, index):
            m = (s + e) // 2
            if (target_a <= s and e <= target_b):
                return segment_tree[index]
            if (target_b < s or e < target_a):
                return 0
            
            return recursive(s, m, index * 2) + recursive(m+1, e, (index * 2) + 1)
        return recursive(1,n,1)      


    mk_tree(1, n, 1)
    for _ in range(k+m):
        a,b,c = map(int, input().split())
        if a==1: #add
            update(b,c)
        else:
            print(calc_sum(b,c))


n, m, k = map(int, input().split())
solution(n,m,k)

