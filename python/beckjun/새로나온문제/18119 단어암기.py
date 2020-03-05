import sys
input = sys.stdin.readline
n, m = map( int, input().split())

words_lis = [input() for _ in range(n)]

query = [list(map(str, input().split())) for _ in range(m)]
alphabet_visited = [1] * (int(ord('z')) + 1)

for i in range(m):
    if query[i][0] == '1':
        alphabet_visited[ord(query[i][1])] = 0
    elif query[i][0] == '2':
        alphabet_visited[ord(query[i][1])] = 1
    # print(alphabet_visited)
    cnt = 0
    for words in words_lis:
        for alphabet in words:
            if alphabet_visited[ord(alphabet)] == 0:
                break
        else:
            cnt += 1
    print(cnt)
