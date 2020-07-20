def findMid(head):
    # Code here
    # return the value stored in the middle node
    temp = head
    length=0
    while temp:
        temp=temp.next
        length+=1
    mid=length // 2
    # print(mid)
    temp = head
    while mid:
        temp=temp.next
        mid-=1
    return temp.data

'''
def findMid(head):
    # Code here
    # return the value stored in the middle node
    fast=head
    slow=head
    
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    
    return slow.data
'''

'''
https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
'''
