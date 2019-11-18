# -*- coding: utf-8 -*-

# @author: Optimus
# @since 2019/11/14


class Solution:
    @staticmethod
    def max_area(height: [int]) -> int:
        max_area = 0
        arr = []
        for i, a in enumerate(height):
            arr.append((a, i))
        arr.sort(key=lambda tup: tup[0], reverse=True)
        arr_len = len(height)
        max_index = arr[0][1]
        min_index = arr[0][1]
        for i, element in enumerate(arr):
            if i > 0:
                curr = element[0] * max(abs(element[1] - min_index), abs(element[1] - max_index))
                if curr > max_area:
                    max_area = curr
                if element[1] > max_index:
                    max_index = element[1]
                if element[1] < min_index:
                    min_index = element[1]
                if element[0] * arr_len < max_area:
                    return max_area
        return max_area


class BestSolution:
    @staticmethod
    def max_area(height: [int]) -> int:
        """
        type height: List[int]
        rtype: int
        """
        height_dict = {index: value for index, value in enumerate(height)}
        result = 0
        j = len(height) - 1
        i = 0
        while j > i:
            if height_dict[j] >= height_dict[i]:
                if (j - i) * min(height_dict[i], height_dict[j]) > result:
                    result = (j - i) * min(height_dict[i], height_dict[j])
                i += 1
            if height_dict[j] < height_dict[i]:
                if (j - i) * min(height_dict[i], height_dict[j]) > result:
                    result = (j - i) * min(height_dict[i], height_dict[j])
                j -= 1

        return result
