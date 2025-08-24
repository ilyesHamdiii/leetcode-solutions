#https://leetcode.com/problems/group-anagrams/description/
# Difficulty:Medium
# Time:o(N)
# 
# # Space:O(N)
# Python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
            