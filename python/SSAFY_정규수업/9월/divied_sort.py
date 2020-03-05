my_list = [69, 10, 30, 2, 16, 8, 31, 22]

def merge(l, r):
    result = []

    while True:
        if len(l) == 0 or len(r) == 0:
            break

        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))

    if len(l) <= 0:
        result.extend(r)

    if len(r) <= 0:
        result.extend(l)

    return result


# def merge_sort(li):
#     mid = len(li) // 2
#
#     lef = li[:mid]
#     rig = li[mid:]
#
#     if len(li) <= 1:
#         return merge(lef, rig)
#
#
#     merge_sort(lef)
#     merge_sort(rig)
#
#
# print(merge_sort(my_list))


def merge_sort(li):
    if len(li) <= 1:
        return li

    mid = len(li) // 2

    lef = li[:mid]
    rig = li[mid:]

    left = merge_sort(lef)
    right = merge_sort(rig)

    return merge(left, right)



print(merge_sort(my_list))

