from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]):
        nums_s = sorted(nums)
        smallerThan = {}
        for i, v in enumerate(nums_s):
            if v not in smallerThan:
                smallerThan[v] = i
            # else:
            #     smallerThan[v] += 1
        result = []
        for i in nums:
            result.append(smallerThan[i])
        return result


solution = Solution()
print(solution.smallerNumbersThanCurrent([1, 1, 1, 2, 3, 4, 5, 8]))
