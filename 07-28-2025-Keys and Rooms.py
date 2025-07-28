#https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75

# Difficulty:Medium

# Time: O(n)

# Space: O(n)
#approach 
""" visit all the possible nodes through depth first traversal
then check if the visited nodes equal to the nodes present in the graph
If they both are the same return TRUE
else Return False """

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited=set()

        def dfs(room):
            visited.add(room)

            for i in rooms[room]:
                if i not in visited:
                    dfs(i)
        dfs(0)
        return len(visited)==len(rooms)
    


        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        