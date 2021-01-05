# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        backPointer = head
        pointer = head
        forthPointer = head
        while forthPointer.next is not None:
            forthPointer = forthPointer.next
            if n > 1:
                n -= 1
            else:
                backPointer = pointer
                pointer = pointer.next
        backPointer.next = pointer.next
        if backPointer == pointer and n == 1:
            head = backPointer.next
        return head
