#https://leetcode.com/problems/count-hills-and-valleys-in-an-array/solutions/?envType=daily-question&envId=2025-07-27

# Difficulty:Easy

# Time: O(n)

# Space: O(n)
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nn=[]
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                nn.append(nums[i])
        
        nums=nn
        count=0
        n=len(nums)
        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                count+=1
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                count +=1
