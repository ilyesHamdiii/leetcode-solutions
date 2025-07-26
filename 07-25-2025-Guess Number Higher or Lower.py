#https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Easy


# Time: O(log(n))
# Space: O(1)
class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1