#https://leetcode.com/problems/subsets/description/

# Difficulty:Medium

# Time: O(n*2^n)

# Space: O(n)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in range(len(nums)):
            res = res + [item+[nums[i]] for item in res]
        return res

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
