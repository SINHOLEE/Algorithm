def reverseList(head):
    # Code here
    if head.next is None:
        return head
    newHead = reverseList(head.next)
    # head.next.next = head
    newHead.next = head

    head = None
    return newHead


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

    def __repr__(self):
        return "data:%s, next:%s" % (self.data, self.next)


class LinkedList:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next


def printList(head: Node):
    temp=head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        n=int(input())
        arr=[int(x) for x in input().split()]
        lis =LinkedList()
        for i in arr:
            lis.insert(i)
        new_head = reverseList(lis.head)
        printList(new_head)