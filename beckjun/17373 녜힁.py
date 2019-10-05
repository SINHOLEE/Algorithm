n, m, q = map(int, input().split())
words = list(map(str, input().split()))
my_list = []
for i in range(n):
    for j in range(i, n):
        if i < j:
            if len(my_list) == 0:
                my_list.append((words[j], words[i]))
            else:
                my_list[-1:] = [my_list[-1], (words[j], words[i])]
        else:
            if len(my_list) == 0:
                my_list.append((words[i], words[j]))
            else:
                my_list[-1:] = [my_list[-1], (words[i], words[j])]
a = sorted(list(my_list))
length = len(a)
for qq in range(q):
    idx = int(input()) - 1
    if idx > length -1:
        print('-1 -1')
    else:
        print(a[idx][0], a[idx][1])