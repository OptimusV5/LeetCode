# -*- coding: utf-8 -*-

# @author: Optimus
# @since 2019-11-13


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ['' for _ in range(numRows)]
        curr = 0
        nxt = 1

        for char in s:
            result[curr] += char
            if curr == numRows - 1:
                nxt = -1
            elif curr == 0:
                nxt = 1
            curr += nxt
        return ''.join(result)

