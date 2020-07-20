class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


cnt = None


def constructTree(pre, preLN, n):
    global cnt
    '''
    Param: pre:  list of Preorder traversal of tree
    param:  preln: list indicating leaf or node
    param: n: no of nodes
    '''
    cnt = 0
    return _constructTree(pre, preLN, n)


def _constructTree(pre, preLN, n):
    global cnt

    if cnt >= n:
        return None
    if preLN[cnt] == "L":
        return Node(pre[cnt])
    new_node = Node(pre[cnt])
    cnt += 1
    new_node.left = _constructTree(pre, preLN, n)
    cnt += 1
    new_node.right = _constructTree(pre, preLN, n)
    return new_node