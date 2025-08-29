#http://leetcode.com/problems/alice-and-bob-playing-flower-game/
# Difficulty:Medium
# Time:o(1)
# 
# # Space:O(1)
# Python
class Solution:
    def flowerGame(self, N :int, M: int) -> int:
        evens_odds=((N+1)//2)*(M//2)
        odds_evens=(N//2)*((M+1)//2)
        return evens_odds+odds_evens