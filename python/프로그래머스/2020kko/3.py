def solution(info, query):
    tree = {}
    db = []
    for a in info:
        db.append(list(a.split()))
    for row in db:
        temp = tree
        for row_idx in range(5):
            if row_idx == 4:
                if temp.get("lis") is None:
                    temp["lis"] = [int(row[row_idx])]

                else:
                    temp["lis"].append(int(row[row_idx]))
            if row_idx < 4 and temp.get(row[row_idx]) is None:
                temp[row[row_idx]] = {}
            if row_idx >= 4:
                continue
            temp = temp[row[row_idx]]
    answer = []
    query_dic = {0: ["cpp", "java", "python"],
                 1: ["backend", "frontend"],
                 2: ["junior", "senior"],
                 3: ["pizza", "chicken"]}


    for i in range(3):
        temp = tree
        if temp.get(query_dic[0][i]) is None:
            continue
        temp1 = temp[query_dic[0][i]]
        for j in range(2):
            if temp1.get(query_dic[1][j]) is None:
                continue
            temp2 = temp1[query_dic[1][j]]
            for k in range(2):
                if temp2.get(query_dic[2][k]) is None:
                    continue
                temp3 = temp2[query_dic[2][k]]
                for t in range(2):
                    if temp3.get(query_dic[3][t]) is not None:
                        temp4 = temp3[query_dic[3][t]]
                        temp4["lis"].sort(reverse=True)

    def dfs(field_idx, temp_tree, q, cnt):
        if field_idx == 4:
            for num in temp_tree["lis"]:  # 반대로
                if int(q[field_idx]) <= num:
                    cnt += 1
                else:
                    break
            else:

                return cnt
        else:
            if q[field_idx] == "-":
                temp_cnt = cnt
                for field in query_dic[field_idx]:
                    if temp_tree.get(field) is not None:
                        cnt += dfs(field_idx + 1, temp_tree[field], q, temp_cnt)
                    else:
                        cnt += 0

            else:
                temp_cnt = cnt
                if temp_tree.get(q[field_idx]) is not None:
                    cnt += dfs(field_idx + 1, temp_tree[q[field_idx]], q, temp_cnt)
                else:
                    cnt += 0
        return cnt

    for q in query:
        q = q.replace("and", "").split()
        cnt = dfs(0, tree, q, 0)
        answer.append(cnt)

    return answer
print(solution(
    ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
))