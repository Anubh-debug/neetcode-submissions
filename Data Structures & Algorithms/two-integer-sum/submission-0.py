class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        indx_lst=[]
        for indx, num in enumerate(nums):
            if target-num in hashmap:
                indx_lst.append(indx)
                indx_lst.append(hashmap[target-num])
                return sorted(indx_lst)
            else:
                hashmap[num]=indx