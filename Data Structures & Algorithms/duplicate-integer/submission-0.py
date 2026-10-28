class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_1={}
        for num in nums:
            if num in dict_1:
                return True
            dict_1[num]=1
        return False