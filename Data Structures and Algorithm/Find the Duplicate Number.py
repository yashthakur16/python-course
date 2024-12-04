class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast=nums[0]
        slow=nums[0]

        fast=nums[nums[fast]]
        slow=nums[slow]

        while(fast!=slow):
            slow=nums[slow]
            fast=nums[nums[fast]]

        slow=nums[0]

        while(fast!=slow):
            slow=nums[slow]
            fast=nums[fast]

        return slow


    
    
        
