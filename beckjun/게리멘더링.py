from pprint import pprint
def check_connect(group, visited):
    my_queue = [group[0]]
    count = 0
    while True:
        if not my_queue:
            break
        node = my_queue.pop(0)
        if visited[node] == False:
            count += 1
            visited[node] = True
            for j in range(len(mat[node])):
                if mat[node][j] == 1 and visited[j] == False and j in group:
                    my_queue.append(j)
    if count == len(group):
        return True
    else:
        return False

def solution(a, b):
    global min_diff, N

    visited = [False] * (N+1)
    check_a = check_connect(a, visited)
    visited = [False] * (N+1)

    check_b = check_connect(b, visited)

    if check_a and check_b:
        sum_a = 0
        sum_b = 0
        for item_a in a:
            sum_a += population[item_a]
        for item_b in b:
            sum_b += population[item_b]

        if min_diff > abs(sum_b - sum_a):
            min_diff = abs(sum_b - sum_a)

    return



def partset(depth, a, b, num):
    global N
    if depth == N:
        total_set.append((a, b))
        return
    partset(depth+1, a + [num], b, num+1)
    partset(depth+1, a, b + [num], num+1)

N = int(input())
my_list = list(map(int, input().split()))
population = [0] * (N+1)
for i in range(1, N+1):
    population[i] = my_list[i-1]
mat=[[0] * (N+1) for _ in range(N+1)]
for j in range(1, N+1):
    temp = list(map(int, input().split()))
    for k in temp[1:]:
        mat[j][k] = 1
        mat[k][j] = 1
group_a = []
group_b = []
total_set = []
partset(0, group_a, group_b,1)
print(total_set)
min_diff = 9999999

for agroup, bgroup in total_set:
    if len(agroup) == 0 or len(bgroup) == 0:
        continue
    solution(agroup, bgroup)

if min_diff == 9999999:
    print(-1)
else:
    print(min_diff)

