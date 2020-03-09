def merge(left, right):
    new_lis = []
    while len(left) != 0 or len(right) != 0:
        if len(left) != 0:
            temp1 = left[0]
        else:
            new_lis.extend(right)
            break
        if len(right) != 0:
            temp2 = right[0]
        else:
            new_lis.extend(left)
            break
        if temp1[0] < temp2[0]:
            a = left.pop(0)
        else:
            if temp1[0] == temp2[0]:
                if temp1[1] <= temp2[1]:
                    a = left.pop(0)
                else:
                    a = right.pop(0)
            else:
                a = right.pop(0)
        new_lis.append(a)
    return new_lis


def merge_sort(lis):
    if len(lis) <= 1:
        return lis
    mid = len(lis) // 2

    left = merge_sort(lis[:mid])
    right = merge_sort(lis[mid:])

    return merge(left, right)


def solution(files):
    answer = []
    temp4 = 0
    for file in files:
        temp1 = ""
        temp2 = ""
        temp3 = ""
        flag = False
        for chrac in file:
            if temp3 == "" and ord('0') <= ord(chrac) <= ord('9'):
                temp2 += chrac
                flag = True
            else:
                if flag:
                    temp3 += chrac
                else:
                    temp1 += chrac
        answer.append((temp1.lower(), int(temp2), temp1+temp2+temp3))
        temp4 += 1
    answer = merge_sort(answer)

    return [arr[2] for arr in answer]


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
