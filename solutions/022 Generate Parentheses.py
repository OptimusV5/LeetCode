# -*- coding: utf-8 -*-

# @author: Optimus
# @since 2019/11/19


class Solution:
    def generate_parenthesis(self, n: int) -> [str]:
        result = []
        visited = set()
        i = n - 1
        j = n
        s = "("
        visited.add(s)
        while s != ")":
            while i > 0 or j > 0:
                if i > 0:
                    if s + "(" not in visited:
                        s += "("
                        i -= 1
                        visited.add(s)
                elif j > 0:
                    if s + ")" not in visited:
                        s += ")"
                        j -= 1
                        visited.add(s)
                    else:
                        break
                if i == 0 and j == 0 and self.is_well_formed(s):
                    result.append(s)
            k = -1
            while s != ")" and s in visited:
                if s[k] == ")":
                    j += 1
                    s = s[:k]
                else:
                    s = s[:k]
                    i += 1
                    if j > 0:
                        s += ")"
                        j -= 1
            visited.add(s)
        return result

    def is_well_formed(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) > 0 and (c == ")" and stack[-1] == "("):
                stack.pop()
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        return False


class BestSolution:
    def generate_parenthesis(self, n: int) -> [str]:
        def place_bracket(open_parens, closed_parens, current):
            if closed_parens == 0 and open_parens == 0:
                result.append(''.join(current))
            elif closed_parens > open_parens:
                place_bracket(open_parens, closed_parens - 1, current + [')'])
                if open_parens > 0:
                    place_bracket(open_parens - 1, closed_parens, current + ['('])
            else:
                place_bracket(open_parens - 1, closed_parens, current + ['('])

        result = []
        place_bracket(n, n, [])
        return result


if __name__ == '__main__':
    solution = BestSolution()
    print(solution.generate_parenthesis(3))
