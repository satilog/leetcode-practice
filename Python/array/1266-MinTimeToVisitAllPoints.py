from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalTime = 0
        for i in range(1, len(points)):
            x_diff = points[i][0] - points[i - 1][0]
            y_diff = points[i][1] - points[i - 1][1]
            totalTime += max(abs(x_diff), abs(y_diff))
        return totalTime


points = [[1, 2], [3, 4], [5, 6]]
solution = Solution()
print(solution.minTimeToVisitAllPoints(points))
# print(points[1:])
