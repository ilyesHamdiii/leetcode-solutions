#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=leetcode-75

# Difficulty:Medium

# Time: O(4\*\*n)

# Space: O(n)

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        n=len(digits)
        res,sol=[],[]
        def backtrack(i):
            if i==n:
                res.append("".join(sol))
                return
            letters={
                "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
            }
            for letter in letters[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()
        backtrack(0)
        return res




        """
        :type digits: str
        :rtype: List[str]
        """

