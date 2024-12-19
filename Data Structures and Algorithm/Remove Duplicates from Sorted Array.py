class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n=len(nums)
        k=0

        for i in range (0,n):
            if(nums[k]==nums[i]):
                continue
            else:
                nums[k+1]=nums[i]
                k+=1

        return  k+1
        
