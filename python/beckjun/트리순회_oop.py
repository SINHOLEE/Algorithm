class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return 'item %s (l %s, r %s)' % (self.item, self.left, self.right)

class Tree:
    def __init__(self):
        self.root = None
        self.dic = {}

    def insert(self, item, l, r):
        if self.root is None:
            self.root = Node(item)
            self.dic[item] = self.root
            self.dic[l] = self.root.left
            self.dic[r] = self.root.right
            print(self.root)
        else:
            self.dic[item] = Node(item)
            self.dic[l] = self.dic[item].left
            self.dic[r] = self.dic[item].right

    def p(self):
        print(self.root)
        print(self.dic)


n = int(input())
bucket = {}
tree = Tree()
for _ in range(n):
    item, l, r = input().split()
    tree.insert(item, l, r)

tree.p()



    # 노드삽입
    # 노드 탐색

# def pre_order(node):
#     print(node, end="")
#     if bucket[node][0] != ".":
#         pre_order(bucket[node][0])
#     if bucket[node][1] != ".":
#         pre_order(bucket[node][1])
#
#
# def in_order(node):
#     if bucket[node][0] != ".":
#         in_order(bucket[node][0])
#     print(node, end="")
#     if bucket[node][1] != ".":
#         in_order(bucket[node][1])
#
#
# def post_order(node):
#     if bucket[node][0] != ".":
#         post_order(bucket[node][0])
#     if bucket[node][1] != ".":
#         post_order(bucket[node][1])
#     print(node, end="")
#
#
#
#
#
#
#
# pre_order("A")
# print()
# in_order("A")
# print()
# post_order("A")
