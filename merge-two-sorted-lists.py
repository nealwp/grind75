"""
Problem:
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list
v1:
    -- the object looks like this:
        ListNode { val: 1, 
            next: ListNode {val: 2, 
                    next: ListNode { val: 4, 
                        next: None
                        }
                    }
                }
    -- create a new list
    -- loop over both lists
    -- compare the value of the two, store the lesser in a new node
    -- advance the list that was used
    -- if one list is longer than the other, handle the leftover

    ** fails on test case [-9, 3], [5, 7] **

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        
        output = ListNode()
        active = output
        
        while list1 and list2:
            if list1.val < list2.val:
                active.next = ListNode(list1.val)
                list1 = list1.next
            else:
                active.next = ListNode(list2.val)
                list2 = list2.next
            active = active.next
        
        if list1:
            active.next = ListNode(list1.val)
            list1 = list1.next
        
        if list2:
            active.next = ListNode(list2.val)
            list2 = list2.next
        
        return output.next
"""
v2:
    -- wrap the remaining list in new while loop
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        
        output = ListNode()
        active = output
        
        while list1 and list2:
            if list1.val < list2.val:
                active.next = ListNode(list1.val)
                list1 = list1.next
            else:
                active.next = ListNode(list2.val)
                list2 = list2.next
            active = active.next
        
        while list1:
            active.next = ListNode(list1.val)
            list1 = list1.next
            active = active.next
        
        while list2:
            active.next = ListNode(list2.val)
            list2 = list2.next
            active = active.next
        
        return output.next

"""
Results:
Runtime: 70 ms, faster than 21.68% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 31.96% of Python3 online submissions for Merge Two Sorted Lists.
"""