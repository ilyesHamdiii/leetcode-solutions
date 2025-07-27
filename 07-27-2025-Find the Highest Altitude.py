#https://leetcode.com/problems/count-hills-and-valleys-in-an-array/solutions/?envType=daily-question&envId=2025-07-27

# Difficulty:Easy

# Time: O(n)

# Space: O(n)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0]*(len(gain)+1)
        res[0]=0
        for i in range(1,len(res)):
            res[i]=gain[i-1]+res[i-1]
        return max(res)
