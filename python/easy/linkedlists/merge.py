from typing import List

def mergeTwoLists(list1, list2):
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    ### dummy node to store result
    dummy = ListNode(0)

    ### tail store last node
    tail = dummy

    while True:
        ### check if either list is empty
        ### if so, join all elements from non-empty  list
        if list1 is None:
            tail.next = list2
            break
        if list2 is None:
            tail.next = list1
            break
        
        ### append shorter list to longer list
        ### and update head
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        ### move tail
        tail = tail.next

    return dummy.next