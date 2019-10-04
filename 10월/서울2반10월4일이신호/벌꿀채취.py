from pprint import pprint
def find_max_honey(lis, result, depth, sum_of_honey):
    global max_res, length, c
    if depth == length:

        if max_res < result and sum_of_honey <= c:
            max_res = result
        return max_res

    find_max_honey(lis, result+(lis[depth][2] ** 2), depth+1, sum_of_honey+lis[depth][2])
    find_max_honey(lis, result, depth + 1, sum_of_honey)
    return max_res
T = int(input())

for tc in range(1,T+1):
    n, m, c = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    # pprint(mat)
    honey_buckets = []
    for i in range(n):
        for j in range(n-m+1):
            temp = []
            for k in range(m):
               temp.append((i, j+k, mat[i][j+k]))
            print(temp)
            max_res = 0
            length = len(temp)

            max_honey = find_max_honey(temp,0, 0, 0)

            honey_buckets.append(temp+[max_honey])
    visited = [[False] * n for _ in range(n)]
    true_max = 0
    ans = 0
    print(honey_buckets)
    for bucket_idx in range(len(honey_buckets)-1):
        for i in range(m):
            visited[honey_buckets[bucket_idx][i][0]][honey_buckets[bucket_idx][i][1]] = True
        for bucket_idx2 in range(bucket_idx+1, len(honey_buckets)):
            count = 1
            for j in range(m):
                if visited[honey_buckets[bucket_idx2][j][0]][honey_buckets[bucket_idx2][j][1]] == True:
                    count += -1
                    break
            if count:
                if true_max < honey_buckets[bucket_idx][-1] + honey_buckets[bucket_idx2][-1]:
                    true_max =  honey_buckets[bucket_idx][-1] + honey_buckets[bucket_idx2][-1]

        for i in range(m):
            visited[honey_buckets[bucket_idx][i][0]][honey_buckets[bucket_idx][i][1]] = False
    print('#%s %s' % (tc, true_max))