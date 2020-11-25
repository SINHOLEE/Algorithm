class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
        self.parent_node = None
    
    def get_parent_node(self):
        return self.parent_node
    
    def set_parent_node(self, node):
        self.parent_node = node

    def delete(self):
        # 1. 자식노드가 하나도 없을 때,
        if self.left_node is None and self.right_node is None:
            if self.value < self.parent_node.value:
                self.parent_node.left_node = None
            elif self.value == self.parent_node.value:
                self.parent_node.left_node = None
                pass
            else:
                self.parent_node.right_node = None
            self.parent_node = None
            return 
        
        # 2 자식노드가 하나 있을 때,
        if self.left_node is None: # 자식노드가 오른쪽만 있을떄
            if self.value <= self.parent_node.value:
                self.parent_node.left_node = self.right_node
            else:
                self.parent_node.right_node = self.right_node
            self.right_node.parent_node = self.parent_node

            self.parent_node = None
            self.right_node = None
            return
        if self.right_node is None:
            if self.value <= self.parent_node.value:
                self.parent_node.left_node = self.left_node
            else:
                self.parent_node.right_node = self.left_node
            self.left_node.parent_node = self.parent_node

            self.parent_node = None
            self.left_node = None
            return
        # 3. 자식노드가 두개 있을 때,
        successer_node = self.right_node.find_min_node_in_sub_tree()
        temp = successer_node.value
        
        successer_node.delete()
        self.value = temp
        return

    def find_min_node_in_sub_tree(self):
        # 이 메소드를 실행하는 순간은, 꼭 자식 노드가 두 개 모두 있을 때, 해당 자식의 오른쪽에서 시작한다.
        # 우리는 루트값을 기준으로 값이 같은 노드도 왼쪽으로 보냈다.
        # 만약 오른쪽에 보냈더라도 해당 메소드는 변할 필요가 없을것...이다?
        # 거의 확실하긴한데 잘 모르겠다.
        if self.left_node is None:
            return self
        return self.left_node.find_min_node_in_sub_tree()

    def __repr__(self):
        return '[%s : %s, %s]' % (self.value, self.left_node, self.right_node)
    
class BinTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.set_root_node(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, cur_node:Node, value):
        if value <= cur_node.value:
            if cur_node.left_node is None:
                new_node = Node(value)
                new_node.set_parent_node(cur_node)
                cur_node.left_node = new_node
            else:
                self.__insert(cur_node.left_node, value)
        else:
            if cur_node.right_node is None:
                new_node = Node(value)
                new_node.set_parent_node(cur_node)
                cur_node.right_node = new_node
            else:
                self.__insert(cur_node.right_node, value)

    def set_root_node(self, value):
        self.root = Node(value)
        
    def my_print(self):
        self.__print(self.root)
        print()

    def __print(self, node:Node):
        if node is None:
            return
        self.__print(node.left_node)
        print(node.value, end=" ")
        self.__print(node.right_node)

    def find(self, value):
        return self.__find(self.root, value)

    def __find(self, currNode:Node, value):
        if currNode is None:
            return None
        elif value < currNode.value:
            return self.__find(currNode.left_node, value)
        elif value > currNode.value:
            return self.__find(currNode.right_node, value)
        return currNode
        
    def delete(self, value):
        node = self.find(value)
        if node is not None:
            node.delete()
            return True
        return False
        

if __name__ == "__main__":
    bt = BinTree()
    arr =[10, 5,3,7,2,4,6,8,9,10,10,10,10,15,13,17,11,14,12,11,11,11,11]
    for i in arr:
        bt.insert(i)
    bt.my_print()
    print(bt.delete(6))
    bt.my_print()
    print(bt.delete(10))
    print(bt.delete(10))
    print(bt.delete(10))
    print(bt.delete(10))
    print(bt.delete(10))
    bt.my_print()
    print(bt.delete(11))
    bt.my_print()
    print(bt.delete(11))
    bt.my_print()
    print(bt.delete(11))
    bt.my_print()
    print(bt.delete(11))
    bt.my_print()
    print(bt.delete(11))
    bt.my_print()
    print(bt.delete(11))
    bt.my_print()
    bt.insert(6)
    bt.my_print()
    bt.insert(10)
    bt.my_print()
    bt.insert(7)
    bt.my_print()
    bt.insert(11)
    bt.my_print()
    bt.insert(6)
    bt.my_print()
    

# reference: https://gist.github.com/jakemmarsh/8273963