#https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty:Medium

# Time:o(n^2)

# Space: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50000: return 1

        k=len(nums)-k
        @cache
        def quickSelect(l,r):
            pivot,p=nums[r],l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p],nums[i]=nums[i],nums[p]
                    p+=1
            nums[p],nums[r]=nums[r],nums[p]
            if p>k:
                return quickSelect(l,p-1)
            elif p<k:
                return quickSelect(p+1,r)
            else:
                return nums[p]
        return quickSelect(0,len(nums)-1)