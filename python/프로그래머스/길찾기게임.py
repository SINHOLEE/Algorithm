import sys
sys.setrecursionlimit(100000)


def solution(nodeinfo):
    pre_order_list = []
    post_order_list = []

    def split_tree(nodes):
        if len(nodes) == 0:
            return
        node = nodes.pop(0)  #
        pre_order_list.append(node[2])
        center = node[0]
        left = []
        right = []
        for no in nodes:
            if no[0] < center:
                left.append(no)
            else:
                right.append(no)

        split_tree(left)
        split_tree(right)
        post_order_list.append(node[2])

    new_nodeinfo = []
    for i in range(len(nodeinfo)):
        new_nodeinfo.append((nodeinfo[i] + [i+1]))
    new_nodeinfo.sort(key=lambda x: x[0])
    new_nodeinfo.sort(key=lambda x: x[1], reverse=True)
    split_tree(new_nodeinfo)
    answer = [pre_order_list, post_order_list]
    return answer


solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
