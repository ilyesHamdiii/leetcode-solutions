# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Difficulty: Medium


# Time: O(n)
# Space: O(n)





class Solution(object):
    def search(self, nums, target):
        if(target not in nums):
            return -1
        else:
            for i in range(len(nums)):
                if (nums[i]==target):
                    return i
        