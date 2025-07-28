#https://leetcode.com/problems/find-the-highest-altitude/description/

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
