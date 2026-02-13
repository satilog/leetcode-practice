class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = cols - 1
        bottom = rows - 1
        top = 0

        result = []

        # Borders closing in approach
        while len(result) < rows * cols:
            # Left to right
            i = left
            while i <= right:
                result.append(matrix[top][i])
                i += 1
            top += 1
            if top > bottom:
                break

            # top to bottom
            i = top
            while i <= bottom:
                result.append(matrix[i][right])
                i += 1
            right -= 1
            if right < left:
                break

            # right to left
            i = right
            while i >= left:
                result.append(matrix[bottom][i])
                i -= 1
            bottom -= 1
            if bottom < top:
                break

            # bottom to top
            i = bottom
            while i >= top:
                result.append(matrix[i][left])
                i -= 1
            left += 1

        return result
