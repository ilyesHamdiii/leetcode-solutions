#https://leetcode.com/problems/reordered-power-of-2/description/

# Difficulty:Medium
# Time: O(n * k) where n is the number of digits in n and k is the number of permutations


# Space:O(n * k) for storing permutations
from itertools import permutations
from ast import List

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
            if n.bit_count() == 1:
                return True
            lst = list(str(n))
            p  = permutations(lst)
            for i in p:
                if i[0] == '0':
                    continue
                n = int(''.join(i))
                if n.bit_count() == 1:
                    return True
            return False
        