class Node:
    def __init__(self, item):
        self.__item = item
        self.__left = None
        self.__right = None

    def __str__(self):
        return "item = %s,  [left = %s, right = %s]" % (self.__item, self.__left, self.__right)

    def set_left(self, item):
        self.__left = item

    def set_right(self, item):
        self.__right = item

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_item(self):
        return self.__item

    def is_equal_item(self, item):
        return True if self.__item == item else False

    def change_node(self, node):
        self.__item = node.get_item()
        self.__left = node.get_left()
        self.__right = node.get_right()


class Tree:
    def __init__(self):
        self.root = None




n = int(input())
bucket = {}
tree = Tree()
for _ in range(n):
    root, l, r = input().split()
    node = Node(root)
    node.set_left(Node(l))
    node.set_right(Node(r))
    tree.insert(node)


    # 노드삽입
    # 노드 탐색

def pre_order(node):
    print(node, end="")
    if bucket[node][0] != ".":
        pre_order(bucket[node][0])
    if bucket[node][1] != ".":
        pre_order(bucket[node][1])


def in_order(node):
    if bucket[node][0] != ".":
        in_order(bucket[node][0])
    print(node, end="")
    if bucket[node][1] != ".":
        in_order(bucket[node][1])


def post_order(node):
    if bucket[node][0] != ".":
        post_order(bucket[node][0])
    if bucket[node][1] != ".":
        post_order(bucket[node][1])
    print(node, end="")







pre_order("A")
print()
in_order("A")
print()
post_order("A")
