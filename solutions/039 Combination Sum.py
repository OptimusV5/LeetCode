# -*- coding: utf-8 -*-

# @author: Optimus
# @since 2019/11/27


class Solution:
    def combination_sum(self, candidates: [int], target: int) -> [[int]]:
        candidates = sorted(candidates)
        return self.combination_local_sum(candidates, target, {})

    def combination_local_sum(self, candidates: [int], target: int, calculated: {}) -> [[int]]:
        retrieved = set()
        result = []
        for i, candidate in enumerate(candidates):
            if candidate < target:
                current_target = target - candidate
                ano_candidates = self.combination_local_sum(candidates[i:], current_target, calculated)
                if len(ano_candidates) > 0:
                    calculated[current_target] = ano_candidates
                if len(ano_candidates) > 0:
                    for ano_can in ano_candidates:
                        temp = [candidate]
                        temp.extend(ano_can)
                        result.append(temp)
                retrieved.add(candidate)
            elif candidate == target:
                result.append([candidate])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combination_sum([5, 10, 8, 4, 3, 12, 9], 27))
