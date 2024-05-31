class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict={}
        for element in nums:
            if element not in my_dict:
                my_dict[element]=0
            else:
                return element
        return -1