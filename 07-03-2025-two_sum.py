# Problem: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy


# Time: O(n)
# Space: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            for j in range (len(nums)):
                if(i==j):
                    continue
                elif(nums[i]+nums[j]==target):
                    return i,j
            

