#https://leetcode.com/problems/house-robber/

# Difficulty:Medium

# Time: O(n)

# Space: O(n)

class Solution(object):
        def rob(self, nums):
                curr,prev=0,0
                for num in nums:
                        prev,curr=curr,max(curr,prev+num)
                return curr

        """
        :type nums: List[int]
        :rtype: int
        """

