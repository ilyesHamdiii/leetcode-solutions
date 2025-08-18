#https://leetcode.com/problems/24-game/description/
# Difficulty:Heart
# Time:o(m*n)
# 
# # Space:O(m*n)
# Python
from fractions import Fraction
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        found=False
        def go(cards):
            if len(cards)==1:
                if cards[0]==24:
                    nonlocal found
                    found=True
                if found:
                    return 
            
            for i in range(len(cards)):
                for j in range(i+1,len(cards)):
                    ncards=cards[:i]+cards[i+1:j]+cards[j+1:]
                    a=cards[i]
                    b=cards[j]
                    ncards.append(a+b)
                    go(ncards)
                    ncards.pop()
                    ncards.append(a-b)
                    go(ncards)
                    ncards.pop()
                    ncards.append(b-a)
                    go(ncards)
                    ncards.pop()
                    ncards.append(a*b)
                    go(ncards)
                    ncards.pop()
                    if b!=0:
                        ncards.append(a/b)
                        go(ncards)
                        ncards.pop()
                    if a!=0:
                        ncards.append(b/a)
                        go(ncards)
                        ncards.pop()
        go(list(Fraction(x) for x in cards))
        return found

                        
                        


        