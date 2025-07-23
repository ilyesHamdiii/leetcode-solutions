# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Easy


# Time: O(n)
# Space: O(n)
class Solution(object):
    def uniqueOccurrences(self, arr):
        x=set()
        res={}
        for i in arr: 
            res[i]=arr.count(i)
        x=set(res.values())
        return len(x)==len(res)
