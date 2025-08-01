#https://leetcode.com/problems/pascals-triangle/description/?envType=daily-question&envId=2025-08-01

# Difficulty:Easy

# Time: O(n*n)

# Space: O(n*n)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1 ,numRows):
            prev = res[-1]
            row = [1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            res.append(row)
        return (res)

        