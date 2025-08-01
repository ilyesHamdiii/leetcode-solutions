#https://leetcode.com/problems/combination-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

# Difficulty:Medium

# Time: O(n)

# Space: O(n)

class Solution(object):
    def combinationSum3(self, k, n):
        if k>n:
            return []
        else:
            res,sol=[],[]
            def backtrack(i=1,summ=0):
                if summ==n and len(sol)==k:
                    res.append(sol[:])
                if summ >n or i==10 or len(sol)==k:
                    return 
                backtrack(i+1,summ)
                sol.append(i)
                backtrack(i+1,summ+i)
                sol.pop()
        backtrack(1,0)
        return res





        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

