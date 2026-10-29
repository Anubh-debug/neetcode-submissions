class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        list_1=[]
        for num in nums:
            if num!=val:
                list_1.append(num)
        for x in range(len(list_1)):
            nums[x]=list_1[x]
        return len(list_1)