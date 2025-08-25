#https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25
# Difficulty:Medium
# Time:o(N)
# 
# # Space:O(N)
# Python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        key = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j >= len(key):
                    key.append([])
                key[i + j].append(mat[i][j])

        res = []
        for i in range(len(key)):
            if i % 2 == 0:
                res.extend(reversed(key[i]))
            else:
                res.extend(key[i])

        return res