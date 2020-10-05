class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data:int):
        if self.head is None:
            self.head = Node(data)
            return
        nodea = self.head


    def print(self):
        temp = self.head
        while True:
            if temp is None:
                break
            print(temp.data, end=" ")
            temp = temp.next

if __name__=='__main__':
    my_sll = SingleLinkedList()
    my_sll.insert(1)
    my_sll.insert(2)
    my_sll.insert(3)
    my_sll.insert(4)
    my_sll.print()