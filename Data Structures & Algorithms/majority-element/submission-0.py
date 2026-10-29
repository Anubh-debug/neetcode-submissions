class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_len=len(nums)//2
        dict_1={}
        for num in nums:
            if num in dict_1:
                dict_1[num]+=1
            else:
                dict_1[num]=1
            if dict_1[num]>maj_len:
                return num