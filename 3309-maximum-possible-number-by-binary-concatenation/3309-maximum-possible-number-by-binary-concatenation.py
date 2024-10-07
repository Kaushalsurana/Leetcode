import itertools
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            arr.append(bin(i)[2:])
        num=0
        for i in itertools.permutations(arr):
            str="".join(i)
            num1=int(str,2)
            num=max(num,num1)
        return num
        # num=""
        # for i in arr:
        #     num+=i
        # res=int(num,2)
        # return res
