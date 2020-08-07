from single_linked_list import LinkedList, Node

def getNth(head, k):
    # Code here
    idx = 0
    temp = head
    while idx != k-1:
        temp = temp.next
        idx += 1
    return temp.data

if __name__ == "__main__":
    T = int(input())
    while T > 0:
        llist = LinkedList()
        n, k = list(map(int, input().split()))
        nodes = list(map(int, input().split()))
        for data in reversed(nodes):
            llist.push(data)
        m = getNth(llist.head, k)
        print(m)
        T -= 1