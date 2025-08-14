#https://leetcode.com/problems/power-of-three/
# Difficulty:Medium
# Time:o(n)

# Space: O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            x=-1
            while True:
                x+=1
                if n==3**x:
                    return True
                    break
                if n<3**x:
                    return False