# -*- coding: utf-8 -*-

# @author: Optimus
# @since 2019/11/25


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        current_node = head
        last_node = None
        while current_node is not None and current_node.next is not None:
            if last_node is not None:
                last_node.next = current_node.next
            else:
                head = current_node.next
            last_node = current_node
            next_node = current_node.next
            current_node.next = current_node.next.next
            next_node.next = current_node
            current_node = current_node.next
        return head
