def delNode(head, k):
    # Code here
    prev = None
    temp = head
    cnt=0
    while cnt != k-1:
        prev = temp
        temp = temp.next
        cnt+=1
    if prev is None:
        head = temp.next
    else:
        prev.next = temp.next

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

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next=Node(data)

def printList(head):
    temp=head
    while temp:
        print(temp.data, end=" ")
        temp=temp.next
    print()


t=int(input())
for i in range(t):
    list1 = LinkedList()
    n=int(input())
    values=list(map(int,input().split()))
    for i in values:
        list1.insert(i)
    k=int(input())
    new_head=delNode(list1.head, k)
    printList(new_head)


'''
input
3
3
1 3 4
3
4
1 5 2 9
2
4
1 5 2 9
1
output
1 3 
1 2 9 
5 2 9 

'''