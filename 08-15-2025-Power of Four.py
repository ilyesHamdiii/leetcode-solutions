#https://leetcode.com/problems/power-of-four/
# Difficulty:Easy
# Time:o(n)
# 
# # Space:O(n)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & (n - 1)) == 0 and n % 3 == 1