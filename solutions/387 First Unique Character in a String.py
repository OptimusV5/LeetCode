# -*- coding: utf-8 -*-
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:

        # build hash map : character and how often it appears
        charSet = collections.Counter(s)

        for index, char in enumerate(s):
            if charSet[char] == 1:
                return index
        return -1
