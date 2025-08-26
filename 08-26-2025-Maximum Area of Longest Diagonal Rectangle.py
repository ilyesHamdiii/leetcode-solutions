#https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/?envType=daily-question&envId=2025-08-26
# Difficulty:Easy
# Time:o(N)
# 
# # Space:O(N)
# Python
class Solution:
    def areaOfMaxDiagonal(self, dm: List[List[int]]) -> int:
        res={}
        n=len(dm)
        for i in range(n):
            diag = (math.sqrt(dm[i][0]*dm[i][0]+dm[i][1]*dm[i][1]))
            ar = dm[i][0] * dm[i][1]
            if diag not in res or res[diag] < ar:
                res[diag] = ar
        return res[max(res)]