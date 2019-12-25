n = int(input())

lis = [*map(int, input().strip().split())]

print(lis)

class tree:
    def __init__(self):
        self.max_cnt = 0
        self.root = None
        self.left = None
        self.right = None
        self.my_cnt = 0

    def insert(self,node):
        if self.root == None:
            self.root = self.node
            self.my_cnt
        else:
