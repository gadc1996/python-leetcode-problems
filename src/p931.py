# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


# Example 1:


# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:


# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.


# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
from typing import List, Tuple


class Solution:
    def __init__(self):
        self.result = {}
        self.matrix_lenght = None

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        results = {}
        for path in self.paths(len(matrix)):
            results[path] = 0
            for i, j in enumerate(path):
                results[path] += matrix[i][int(j)]
                
        values = results.values()
        min_value = min(value for value in values)
        
        return min_value if min_value in values else -min_value
        
    def paths(self, depth: int) -> List[str]:
        indexes = [str(i) for i in range(0, depth)]
        results = []
        n = depth
        for i in indexes:
            results += self._paths_recursive(i, depth, n)

        return results

    def _paths_recursive(self, i: str, depth: int, n: int) -> List[str]:
        if depth == 1:
            return [i]
        else:
            return [f"{i}{item}" for item in self._paths_recursive(i, depth - 1, n)] + [
                f"{i}{item}"
                for item in self._paths_recursive(int(i) + 1, depth - 1, n)
                if int(i) + 1 < n
            ] + [
                f"{i}{item}"
                for item in self._paths_recursive(int(i) - 1, depth - 1, n)
                if int(i) - 1 >= 0
            ]


    # def paths(self, depth: int) -> List[str]:
    #     indexes = [str(i) for i in range(0, depth)]
    #     results = []
    #     n = depth
    #     for i in indexes:
    #         results += self._paths_recursive(i, depth, n)

    #     return results

    # def _paths_recursive(self, i: str, depth: int, n: int) -> List[str]:
    #     if depth == 1:
    #         return [i]
    #     else:
    #         return [f"{i}{item}" for item in self._paths_recursive(i, depth - 1, n)] + [
    #             f"{i}{item}"
    #             for item in self._paths_recursive(int(i) + 1, depth - 1, n)
    #             if int(i) + 1 < n
    #         ] + [
    #             f"{i}{item}"
    #             for item in self._paths_recursive(int(i) - 1, depth - 1, n)
    #             if int(i) - 1 >= 0
    #         ]