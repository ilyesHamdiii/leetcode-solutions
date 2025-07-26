#https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/?envType=daily-question&envId=2025-07-25
# Difficulty: Easy


# Time: O(nlog(n))
# Space: O(n)
class Solution:
    def maxSum(self, nums):
        s = set(nums)
        result = sum(x for x in s if x > 0)
        if result == 0:
            result = max(s)
        return result