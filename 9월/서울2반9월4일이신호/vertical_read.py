T = int(input())

for tc in range(1, T + 1):
    mat = []
    max_len = 0
    for i in range(5):
        words = list(input())
        mat.append(words)
        if len(words) >= max_len:
            max_len = len(words)
    print('#%s' % tc, end=' ')
    for j in range(max_len):
        for i in range(5):
            if len(mat[i]) - 1 < j:
                pass

            else:
                print(mat[i][j], end = '')

    print()