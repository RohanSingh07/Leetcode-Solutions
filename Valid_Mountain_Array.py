# Two pointer solution
# Time complexity O(n) Single pass
# Space complexity O(1)
# Left pointer will proceed forward till it find an element less than the current one
# Right pointer will proceed backward till in find an element less than the current one

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        le = len(arr)
        if le<3 or arr[0]>arr[1] or arr[-1]>arr[-2]:
            return False
        
        l,r =0,le-1
        count = 0
        while l<le-1:
            if arr[l]<arr[l+1]:
                count+=1
                l+=1
            else:
                break
        while r>0:
            if arr[r]<arr[r-1]:
                count+=1
                r-=1
            else:
                break
        if count == le-1:
            return True
        else:
            return False
            
