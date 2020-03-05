preorder = [[-1]] + [[] for _ in range(10000)]
count = 0
while True:
    try:
        n = int(input())
        count += 1
        if count == 1:
            preorder[1].append(n)
        else:


    except:
        break
print(preorder)

