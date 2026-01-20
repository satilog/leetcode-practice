from typing import List


class Solution:
    # Big O: O(n^2)
    def missingNumber(self, nums: List[int]):
        uniqueVals = set(nums)
        for i in range(len(nums) + 1):
            if i not in uniqueVals:
                return i


solution = Solution()
print(solution.findMissingNumber([0, 1, 2, 3, 4, 5, 7]))
