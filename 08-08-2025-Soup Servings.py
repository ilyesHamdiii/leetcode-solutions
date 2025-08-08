#https://leetcode.com/problems/soup-servings/description/

# Difficulty:Medium

# Time: O(n^2)

# Space: O(n^2)

class Solution:
    def soupServings(self, n: int) -> float:
        if n>5000:
            return 1
        @cache
        def soup(a,b):

            if 0>=a and 0>=b:
                return 0.5
            if 0>=b:
                return 0
            if 0>=a:
                return 1
            res=0
            res+=0.25*soup(a-100,b)
            res+=0.25*soup(a-75,b-25)
            res+=0.25*soup(a-50,b-50)
            res+=0.25*soup(a-25,b-75)
            return res
        return soup(n,n)

