# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Easy


# Time: O(n)
# Space: O(n)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and char == s[i]:
                i+=1
        return i == len(s)
        