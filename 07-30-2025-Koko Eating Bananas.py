#https://leetcode.com/problems/koko-eating-bananas/?envType=study-plan-v2&envId=leetcode-75

# Difficulty:Medium

# Time: O(n)
import math
# Space: O(n)

class Solution(object):
    def minEatingSpeed(self, piles, h):
        k=1
        low, high = 1, 10 
        while low <= high:
            k = (low + high) // 2
            if sum(math.ceil(1.0 _ pile / k) for pile in piles) > h: low = k + 1
            else: high = k - 1
        return low
