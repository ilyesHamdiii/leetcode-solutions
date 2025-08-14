#https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
# Difficulty:Easy
# Time:o(n)

# Space:O(1)
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=["999","888","777","666","555","444","333","222","111","000"]
        for i in res:
            if i in num:
                return i
        return ""