class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set()
        ans=0
        n=len(nums)

        for i in range (0,n):
            st.add(nums[i])

        for i in st:
            if(i-1 in st):
                continue
            else:
                cnt=1
                num=i+1
                while(num in st):
                    cnt+=1
                    num+=1
                    
                ans=max(ans,cnt)

        return ans
                    
