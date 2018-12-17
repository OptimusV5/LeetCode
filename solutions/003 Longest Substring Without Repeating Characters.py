# -*- coding: utf-8 -*-

# @author: Optimus
# @since 2018-12-15


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        last_chars = {}
        start_index = 0
        for index, char in enumerate(s):
            if char in last_chars.keys():
                last_index = last_chars[char]
                if last_index >= start_index:
                    start_index = last_index + 1
            last_chars[char] = index

            now_len = index - start_index + 1
            if max_len < now_len:
                max_len = now_len
        return max_len
