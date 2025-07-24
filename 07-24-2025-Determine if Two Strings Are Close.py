# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Medium


# Time: O(n)
# Space: O(n)
from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        c1=Counter(word1)
        c2=Counter(word2)
        n1=Counter([v for v in c1.values()])
        n2=Counter([v for v in c2.values()])
        return c1==c2 or (n1==n2 and set(word1)==set(word2))


        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        