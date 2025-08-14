#https://leetcode.com/problems/smallest-number-in-infinite-set/
# Difficulty:MEdium
# Time:o(n)

# Space:O(1)
class SmallestInfiniteSet:

    def __init__(self):
        self.res=[]
        for i in range(1,1001):
            self.res.append(i)

    def popSmallest(self) -> int:
        if not self.res:return 
        x=self.res.pop(self.res.index(min(self.res)))
        return x
        
        

    def addBack(self, num: int) -> None:
        if num in self.res:
            return 
        else:
           self.res.append(num)
           self.res.sort()

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)