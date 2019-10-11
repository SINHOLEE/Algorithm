class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:  # 전위순회방식으로 생성
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if node.value < value: # value가 저장하려는 숫자. 작으면 왼쪽 , 크면 오른쪽
            if node.left == None:
                node.left = Node(value)
            else:  # left에 Node가 있으면 그 아래에 저장
                self._add(value, node.left)
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                self._add(value, node.right)

    def printAll(self):  # 전위순회방식
        if self.root == None:
            return
        self._print(self.root)


    def _print(self, node):
        if node != None:
            print(node.value)  # 전위
            self._print(node.left)
            self._print(node.right)

    # def _print(self, node):
    #     if node != None:
    #         self._print(node.left)
    #         print(node.value)  # 중위
    #         self._print(node.right)
    #
    # def _print(self, node):
    #     if node != None:
    #         self._print(node.left)
    #         self._print(node.right)
    #         print(node.value)  # 후위

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node == None:
            return False
        if node.value == key:
            return True
        elif node.value < key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)


t = Tree()
t.add(5)
t.add(2)
t.add(4)
t.add(3)

t.printAll()  # 전체저장값 출력하기 (전위, 중위, 후위 검색)

print(t.find())