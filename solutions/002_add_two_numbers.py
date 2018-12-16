# -*- coding: utf-8 -*-

# @author: Optimus
# @since 2018-12-15

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        results = []
        addition = 0
        while l1 and l2:
            digit_add = l1.val + l2.val + addition
            # try divmod
            addition = digit_add // 10
            results.append(digit_add % 10)
            l1 = l1.next
            l2 = l2.next

        l3 = l1 if l1 else l2

        while l3:
            digit_add = l3.val + addition
            addition = digit_add // 10
            results.append(digit_add % 10)
            l3 = l3.next

        if addition:
            results.append(addition)

        return results
