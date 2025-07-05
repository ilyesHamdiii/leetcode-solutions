# Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Difficulty: Medium


# Time: O(n)
# Space: O(n)
class Solution(object):
       
    def searchRange(self, nums, target,i=0,k=0):
        if(target not in nums):
            return [-1,-1]
        else:
            if(len(nums)==1):
                return [0,0]
        for i in range (len(nums)):
            if(nums[i]==target):
                
                if(nums.count(target)>2):
                    for j in range (len(nums)-1,i,-1):
                         if(target==nums[j]):
                            break
                    return[i,j]
                elif(nums.count(target)>1):

                    return [i,i+1]
                else:
                    return [i,i]
                