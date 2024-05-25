class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxelem=max(nums)
        cnt=0
        subcnt=0
        l=0
        for num in nums:
            if num==maxelem:
                cnt+=1
            while cnt>=k:
                if nums[l]==maxelem:
                    cnt-=1
                l+=1
            subcnt+=l
        return subcnt