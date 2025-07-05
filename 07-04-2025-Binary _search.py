# Problem: https://leetcode.com/problems/binary-search/description/
# Difficulty: Easy


# Time: O(n)
# Space: O(n)
class Solution(object):
    def search(self, nums, target):
        for i in range (len(nums)):
            if nums[i]==target:
                return i
        return -1
