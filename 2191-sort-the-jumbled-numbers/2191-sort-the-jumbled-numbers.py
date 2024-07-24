class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        null=[]
        for num in nums:
            curr=0
            num=str(num)
            for i in range(len(num)):
                curr=curr*10+mapping[int(num[i])]
            null.append(curr)
        print(null)

        idx=[i for i in range(len(null))]
        idx.sort(key=lambda x:null[x])
        print(idx)
        res=[]
        for index in idx:
            res.append(nums[index])
        return res