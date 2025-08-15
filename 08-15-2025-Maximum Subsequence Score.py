#https://leetcode.com/problems/maximum-subsequence-score/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty:MEdium
# Time:nlog(n)
# 
# # Space:O(k)
from heapq import heappush, heappop
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []

        res = total = 0
        for a, b in sorted(list(zip(nums1, nums2)), key = lambda ab: -ab[1]):
            heappush(heap, a)
            total += a
            if len(heap) > k: total -= heappop(heap)
            if len(heap) == k: res = max(res, total * b)
        return res