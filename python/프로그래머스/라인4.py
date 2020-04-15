def solution(snapshots, transactions):
    sn_dic = {}
    for sn in snapshots:
        if sn_dic.get(sn[0]) is None:
            sn_dic[sn[0]] = int(sn[1])

    transet = set()
    for ts in transactions:
        if ts[0] not in transet:
            if sn_dic.get(ts[2]) is None:
                sn_dic[ts[2]] = 0
            if ts[1] == 'SAVE':
                sn_dic[ts[2]] += int(ts[3])
            else:
                sn_dic[ts[2]] -= int(ts[3])
        transet.add(ts[0])
    answer = []
    for k, item in sn_dic.items():
        answer.append([k, str(item)])

    return answer


print(solution([
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
], [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]
)
)
