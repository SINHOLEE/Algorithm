# if __name__ == "__main__":
n = int(input())
adj_list = [[] for _ in range(n+1)]
tasks = [0] * (n+1)
inner_degree = [0] * (n+1)
dp = [0] * (n+1)
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    tasks[i] = temp[0]
    for _ in range(temp[1]):
        adj_list[temp[_+2]].append(i)
        inner_degree[i] += 1
        
print(adj_list)
print(tasks)
print(inner_degree)