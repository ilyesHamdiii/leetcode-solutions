#https://leetcode.com/problems/implement-trie-prefix-tree/description/
# Difficulty:Medium
# Time:o(N)
# 
# # Space:O(N)
# Python
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        mnx=R
        mxx=0
        mny=C
        mxy=0

        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    mnx=min(mnx,i)
                    mxx=max(mxx,i)
                    mny=min(mny,j)
                    mxy=max(mxy,j)
        return (mxx-mnx+1)*(mxy-mny+1)
        