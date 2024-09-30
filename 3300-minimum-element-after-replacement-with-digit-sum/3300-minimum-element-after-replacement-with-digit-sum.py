class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            sum=0
            while i:
                k=i%10
                sum+=k
                i=i//10
            arr.append(sum)
        arr.sort()
        return arr[0]
            
