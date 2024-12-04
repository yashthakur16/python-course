class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index=-1
        
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<nums[i+1]):
                index=i
                break

        if(index==-1):
            nums.sort()
            return

        for i in range(len(nums)-1,-1,-1):
            if(nums[index]<nums[i]):
                temp=nums[index]
                nums[index]=nums[i]
                nums[i]=temp
                break

        nums[index+1:len(nums)]=nums[index+1:len(nums)][::-1]

        return

        
        
