from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]):
        missingVals = set(range(1, len(nums) + 1))
        for i in nums:
            if i in missingVals:
                missingVals.remove(i)
        return list(missingVals)


solution = Solution()
print(solution.findDisappearedNumbers([1, 1, 1, 2, 3, 4, 5, 8]))
