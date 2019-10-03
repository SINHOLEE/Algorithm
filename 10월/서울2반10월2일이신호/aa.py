temp = []
for i in range(200):
    if i < 100:
        temp.append(input())
    else:
        a = input()
        if a not in temp:
            print(a)