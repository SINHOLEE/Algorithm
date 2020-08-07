from single_linked_list import LinkedList, Node

def getCount(head_node):
    #code here
    cnt = 0
    temp = head_node
    while temp != None:
        cnt+=1
        temp = temp.next
    return cnt


if __name__ == '__main__':
    # t = int(input())
    # for cases in range(t):
    n = int(input())
    a = LinkedList()
    nodes = list(map(int, input().strip().split()))
    for data in nodes:
        node = Node(data)
        a.append(node)
    print(getCount(a.head))