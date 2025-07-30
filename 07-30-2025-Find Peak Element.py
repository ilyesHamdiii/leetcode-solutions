#https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

# Difficulty:Medium

# Time: O(1)

# Space: O(n)   
class Solution(object):
    def findPeakElement(self, nums):
        return nums.index(max(nums))

        """
        :type nums: List[int]
        :rtype: int
        """
        