#Your task is to complete this function
 
class Solution:
    def maxLen(self, arr):
        mpp={}
        maxi=0
        sumi=0;
        n=len(arr)
        
        for i in range(0,n):
            sumi+=arr[i]
            
            if (sumi==0):
                maxi=i+1
                mpp[sumi]=i
            elif sumi in mpp:
                maxi=max(maxi,i-mpp[sumi])
            elif sumi not in mpp:
                mpp[sumi]=i
                
        
        return maxi
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(arr))
        print("~")

# } Driver Code Ends
