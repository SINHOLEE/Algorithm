import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('result.txt', 'w', encoding='utf-8')

for t in range(1, 11):
    T = int(input())
    building_list = list(map(int, input().split()))
    result = 0
    for i in range(2, len(building_list) - 2):
        a = building_list[i] - building_list[i - 1]
        b = building_list[i] - building_list[i - 2]
        c = building_list[i] - building_list[i + 1]
        d = building_list[i] - building_list[i + 2]

        my_sorting_list = [a, b, c, d]

        temp = 0
        for j in range(len(my_sorting_list)):
            if j == 0:
                temp = my_sorting_list[j]
            else:
                if temp > my_sorting_list[j]:
                    temp = my_sorting_list[j]
                else:
                    pass
        if temp > 0:
            pass
        else:
            temp = 0
        result += temp

    print('#', end='')
    print(t, result)






