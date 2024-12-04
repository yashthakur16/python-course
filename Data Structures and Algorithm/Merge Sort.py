class Solution:

    def merge(self,nums,start,end):

        mid=int((start+end)/2)
        length1=mid-start+1
        length2=end-mid

        l1=[]
        l2=[]

        k=start
        i=0
        j=0

        while(i<length1):
            l1.append(nums[k])
            k+=1
            i+=1
        
        while(j<length2):
            l2.append(nums[k])
            k+=1
            j+=1

        i=0
        j=0
        k=start

        while(i<length1 and j<length2):
            if(l1[i]<l2[j]):
                nums[k]=l1[i]
                k+=1
                i+=1
            else:
                nums[k]=l2[j]
                k+=1
                j+=1
        
        while(i<length1):
            nums[k]=l1[i]
            k+=1
            i+=1

        while(j<length2):
            nums[k]=l2[j]
            k+=1
            j+=1

        return



    def merge_sort(self,nums,start,end):
        if(start>=end):
            return

        mid=int((start+end)/2)

        self.merge_sort(nums,start,mid)
        self.merge_sort(nums,mid+1,end)

        self.merge(nums,start,end)
        return

    def sortArray(self, nums: List[int]) -> List[int]:
        end=len(nums)-1
        self.merge_sort(nums,0,end)
        return nums
        
