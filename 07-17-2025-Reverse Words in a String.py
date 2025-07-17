# Problem:https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Medium


# Time: O(n)
# Space: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        string=""
        s=' '.join(s.strip().split())
        res=s.split()
        for i in res:
            string=i+" "+string
        return string.strip()


