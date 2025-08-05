#https://leetcode.com/problems/fruits-into-baskets-ii/

# Difficulty:Easy

# Time: O(n)

# Space: O(n)

class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        x=0
        for i in range(len(fruits)):
            for j in range(len(fruits)):
                if fruits[i]<=baskets[j]:
                    x+=1
                    baskets[j]=-9
                    break
                    
        return len(fruits)-x
        


        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        
