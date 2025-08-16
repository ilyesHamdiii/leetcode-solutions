#https://leetcode.com/problems/maximum-69-number/
# Difficulty:Easy
# Time:o(n)
# 
# # Space:O(n)
# Python
class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))