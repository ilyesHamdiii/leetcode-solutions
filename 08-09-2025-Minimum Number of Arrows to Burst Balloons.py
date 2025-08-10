#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=leetcode-75

# Difficulty:Medium

# Time: O(n log n)

# Space: O(1)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res=len(points)

        prev=points[0]
        for i in range(1,len(points)):
            curr=points[i]
            if prev[1]>=curr[0]:
                res-=1
                prev=[curr[0],min(curr[1],prev[1])]

            else:
                prev=curr
        return res