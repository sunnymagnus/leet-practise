class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sm =0
        n=len(nums)
        for i in range(1,n+1):
            sm+=i
        
        return sm-sum(nums)
        