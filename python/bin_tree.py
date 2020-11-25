from pprint import pprint
import json


class Node:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
    
    def __repr__(self):
        return '%s : [%s, %s]' % (self.value, self.leftNode, self.rightNode)
    
class BinTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.setRootNode(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, curNode:Node, value):
        if value <= curNode.value:
            if curNode.leftNode is None:
                curNode.leftNode = Node(value)
            else:
                self.__insert(curNode.leftNode, value)
        else:
            if curNode.rightNode is None:
                curNode.rightNode = Node(value)
            else:
                self.__insert(curNode.rightNode, value)


    def setRootNode(self, value):
        self.root = Node(value)
        
    def myPrint(self):
        self._print(self.root)
        print()

    def _print(self, node:Node):
        if node is None:
            return
        self._print(node.leftNode)
        print(node.value, end=" ")
        self._print(node.rightNode)

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, currNode:Node, value):
        if currNode is None:
            return None
        elif currNode.value == value:
            return currNode
        elif value < currNode.value:
            return self._find(currNode.leftNode, value)
        elif value > currNode.value:
            return self._find(currNode.rightNode, value)
        



if __name__ == "__main__":
    bt = BinTree()
    bt.insert(7)
    bt.insert(3)
    bt.insert(1)
    bt.insert(2)
    bt.insert(7)
    bt.insert(6)
    bt.insert(5)
    bt.insert(8)
    bt.insert(9)
    bt.insert(8)
    bt.insert(3)

    bt.myPrint()
    for i in range(10):
        print(i, bt.find(i))