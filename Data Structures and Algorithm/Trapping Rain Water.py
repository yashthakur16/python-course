class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lmax=0
        rmax=0
        water=0

        while(l<r):
            if(height[l]<=height[r]):
                if(height[l]<lmax):
                    water=water+(lmax-height[l])
                else:
                    lmax=max(lmax,height[l])
                l+=1
            else:
                if(height[r]<rmax):
                    water=water+(rmax-height[r])
                else:
                    rmax=max(rmax,height[r])
                r-=1

        
        return water
                

        
