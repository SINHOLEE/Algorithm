def insertAtBegining(head, x):
    temp = head
    head = Node(x)
    head.next = temp
    return head
# function appends data x at the end of list and returns new head
def insertAtEnd(head, x):
    # code here
    if head is None:
        head = Node(x)
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = Node(x)
    return head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "{data: %s, next: %s}" % (self.data, self.next)


class LinkedList:
    def __init__(self):
        self.head = None


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


t = int(input())
for cases in range(t):
    n=int(input())
    a=LinkedList()

    nodes_info = list(map(int, input().split()))
    for i in range(0, len(nodes_info)-1, 2):
        if nodes_info[i+1]:
            a.head = insertAtEnd(a.head, nodes_info[i])
        else:
            a.head = insertAtBegining(a.head, nodes_info[i])

    printList(a.head)