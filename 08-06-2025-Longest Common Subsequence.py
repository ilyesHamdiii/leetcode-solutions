#https://leetcode.com/problems/longest-common-subsequence/description/

# Difficulty:Medium

# Time: O(mn)

# Space: O(mn)

import functools
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):

        m=len(text1)
        n=len(text2)
        @functools.cache
        def sub(i,j):
            if i==m or j==n:
                return 0
            else:
                if text1[i]==text2[j]:
                    return 1+sub(i+1,j+1)
                else:
                    return max(sub(i,j+1),sub(i+1,j))
        return sub(0,0)