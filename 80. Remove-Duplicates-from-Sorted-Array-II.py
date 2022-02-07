# Two Pointer solution 
# Keep one pointer at the node until where everything before are fine and keep replacing if you find i'th node to be different than index-2th node

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l<3:
            return l
        ind = 2
        for i in range(2,l):
            if nums[i] != nums[ind-1]:
                nums[ind] = nums[i]
                ind+=1
        return ind
            
