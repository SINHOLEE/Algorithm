

# def main(n,mat):
#     ab = []
#     cd = []
#     for i in range(n):
#         for j in range(n):
#             ab.append(mat[i][0]+mat[j][1])
#             cd.append(mat[i][2]+mat[j][3])
#     ab.sort()
#     cd.sort()
#     answer = 0
#     s= 0
#     e = len(cd)-1
#     while s< len(cd) or e>=0:
#         while s<len(ab) and ab[s]<cd[e]:
#             s+=1
#         if(ab[s]+cd[e]==0):
#             answer+=1
#         while e >= 0 and ab[s]> cd[e]:
#             e-=1
#         if(ab[s]+cd[e]==0):
#             answer+=1

#     return answer
# if __name__ == '__main__':
#     n = int(input())
#     mat = [[*map(int, input().split(" "))] for _ in range(n)]
#     print(main(n, mat))
    
import sys
input = sys.stdin.readline

# 이분탐색
def upper_bound(target, lis):
    s = 0
    e = len(lis)
    answer = -1
    while s<e:
        m = (s+e)//2
        if target >= lis[m]:
            s= m+1
        else :
            e = m
    return s

def lower_bound(target, lis):
    s = 0
    e = len(lis)
    while s<e:
        m = (s+e)//2
        if target > lis[m]:
            s= m+1
        else:
            e = m
            
    return s

def main(n,mat):
    ab = [0]*(n**2)
    cd = [0]*(n**2)
    for i in range(n):
        for j in range(n):
            ab[i*n + j] =mat[i][0]+mat[j][1]
            cd[i*n + j]= mat[i][2]+mat[j][3]
    cd.sort()
    answer = 0
    for num in ab:
        upper_idx = upper_bound(-1*num,cd)
        lower_idx = lower_bound(-1*num, cd)
        if(cd[lower_idx] == -1 * num ):
            answer += upper_idx - lower_idx
        
    return answer
if __name__ == '__main__':
    n = int(input())
    mat = [[*map(int, input().split(" "))] for _ in range(n)]
    print(main(n, mat))