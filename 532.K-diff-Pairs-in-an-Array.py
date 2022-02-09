# Create a hashmap with all the elements and their respective counts
# iterate throught the hashmap items and check if there exists another element with key+k value
# That means there is another element with the required value 

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        hashmap = Counter(nums)
        if k==0:
            for key,value in hashmap.items():
                if value>1:
                    count+=1
        else:
            for key,value in hashmap.items():
                if key+k in hashmap:
                    count+=1
        return count
