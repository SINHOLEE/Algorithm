n, q = map(int, input().split())

dic_i = {}
dic_j = {}
dic_total = {}
for num in range(1, n+1):
    i, j = map(int, input().split())
    dic_total[num] = [(i, j), 1]
    if i not in dic_i:
        dic_i[i] = [[i, j, num, 1]]
    else:
        dic_i[i][-1:] = [dic_i[i][-1], [i, j, num, 1]]
    if j not in dic_j:
        dic_j[j] = [[i, j, num, 1]]
    else:
        dic_j[j][-1:] = [dic_j[j][-1], [i, j, num, 1]]

print(dic_i)
print(dic_j)
print(dic_total)