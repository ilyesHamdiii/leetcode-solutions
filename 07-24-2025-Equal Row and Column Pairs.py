# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Medium


# Time: O(n)
# Space: O(n*n*n)
class Solution:
    def equalPairs(self, grid) :
        n = len(grid)
        pairs = 0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        break
                else:
                    pairs += 1

        return pairs