# -*- coding: utf-8 -*-

# @author: Optimus
# @since 2018-12-15


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index_map = {}
        for index, num in enumerate(nums):
            if num in num_index_map.keys():
                return [num_index_map[num], index]
            else:
                num_index_map[target - num] = index
