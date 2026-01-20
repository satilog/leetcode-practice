import math
from typing import List


class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     uniqueVals = set()
    #     for i in nums:
    #         print(i)
    #         if i in uniqueVals:
    #             return True
    #         uniqueVals.add(i)
    #     return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 4]))
