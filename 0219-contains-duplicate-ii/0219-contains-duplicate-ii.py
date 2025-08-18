class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a=set()
        b=0
        for i in range(len(nums)):
            if i-b>k:
                a.remove(nums[b])
                b+=1
            if nums[i] in a:
                return True
            a.add(nums[i])
        return False