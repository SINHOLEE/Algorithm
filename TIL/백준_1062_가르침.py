def combi(i, depth):
    global max_cnt
    if depth == k-5:
        cnt = 0
        for word in words:
            for char in word:
                if visited[ord(char) - ord('a')] == 0:
                    break
            else:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
        return
    for jj in range(i, 26):
        if visited[jj]:
            continue
        visited[jj] = 1
        combi(jj, depth+1)
        visited[jj] = 0


visited = [0] * 26
for j in range(26):
    if j == 0 or j == ord("c")-ord("a") or j == ord("n")-ord("a") or j == ord("t")-ord("a") or j == ord("i")-ord("a"):
        visited[j] = 1
n, k = map(int, input().split())
words = [list(input()) for _ in range(n)]
max_cnt = 0
if k > 4:
    combi(0, 0)
print(max_cnt)
