def perm(depth,lis):
    global visited
    if depth == len(nums):
        print(lis)
        return
    for i in range(len(nums)):
        if visited & 1 << i:
            continue
        # temp = visited
        visited = visited | 1 << i
        perm(depth+1, lis+[nums[i]])
        visited = not (-1*(visited-1) & 1 << i)
        # visited = temp
visited = 0
nums = [1,2,3]
perm(0,[])