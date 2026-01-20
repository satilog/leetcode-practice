from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        indexLookup = {}
        for i, v in enumerate(nums):
            if (target - v) not in indexLookup:
                indexLookup[v] = i
            else:
                return i, indexLookup[target - v]
