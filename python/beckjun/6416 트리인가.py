def bfs(node):
    global tree
    q = [node]
    while q:
        node = q.pop(0)
        if adj_list.get(node) is None:
            continue
        for nxt in adj_list[node]:
            if visited[nxt]:
                tree = False
                q = []
                break
            visited[nxt] += 1
            q.append(nxt)


flag = True
rnd = 0
while flag:
    tree = True
    adj_list = {}
    in_degree = {}
    nodes = set()
    stop_loop = True
    while stop_loop:
        line = input()
        if line == "-1 -1":
            flag = False
            break

        line_list = list(line.split(" "))
        line_list = list(filter(lambda x: x != "", line_list))
        for i in range(0, len(line_list), 2):
            a = line_list[i]
            b = line_list[i+1]
            if a == "0" and b == "0":
                stop_loop = False
                rnd += 1
                break
            # adj_lis
            if adj_list.get(a) is not None:
                adj_list[a].append(b)
            else:
                adj_list[a] = [b]
            # make set
            nodes.add(a)
            nodes.add(b)

            # make indegree
            if in_degree.get(b) is not None:
                tree = False
                in_degree[b] += 1
            else:
                in_degree[b] = 1
    if not flag:
        break
    # 여기서부터 시작
    # 근데 너무 예외케이스하나하나를 다뤄야한다 내코드는...
    root = None
    for node in nodes:
        if in_degree.get(node) is None:
            root = node
    visited = {}
    for node in nodes:
        visited[node] = 0
    # print(adj_list)
    # print(root)
    if nodes.__len__():
        if root is None:
            tree = False
        else:
            bfs(root)
        cnt = 0
        for k, v in visited.items():
            if v == 0:
                cnt += 1
        if cnt > 1:
            tree = False
        if cnt == 0:
            tree = False

    # print(visited)
    # print(line_list)
    if tree:
        print("Case %s is a tree." % rnd)
    else:
        print("Case %s is not a tree." % rnd)
    # print(in_degree)
    # print(nodes)
    # print()