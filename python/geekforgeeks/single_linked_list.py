class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, new_node):  # tail에 새로운 item을 덧 붙이는 방식
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next

    def push(self, new_data):  # head에 새로운 item을 덧 붙이는 방식
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node