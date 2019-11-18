# -*- coding: utf-8 -*-

# @author: Optimus
# @since 2019/11/18


class Solution:
    @staticmethod
    def int_to_roman(num: int) -> str:
        int_to_roman_arr = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        roman = ""
        for tup in int_to_roman_arr:
            roman += tup[1] * (num // tup[0])
            num = num % tup[0]
        return roman

