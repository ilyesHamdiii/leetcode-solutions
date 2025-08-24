#https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/description/
# Difficulty:Hard
# Time:O(N∗M∗M∗M)
# 
# # Space:O(N)
# Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        else:
            

            def pal(x):
                if len(x)==0 or len(x)==1:
                    return True
                elif x[0]==x[-1]:
                    return pal(x[1:len(x)-1])
                else:
                    return False
            return pal(str(x))

        
            