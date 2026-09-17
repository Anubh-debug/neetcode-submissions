class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ar1=[1]
        ar2=[1]
        ar3=[]
        for i in range(1, len(nums)):
            if i<=1:
                ar1.append(nums[i-1])
            else:
                ar1.append(nums[i-1]*ar1[i-1])
        nums=nums[::-1]
        for i in range(1, len(nums)):
            if i<=1:
                ar2.append(nums[i-1])
            else:
                ar2.append(nums[i-1]*ar2[i-1])
        ar2=ar2[::-1]

        for x, y in zip(ar1,ar2):

            ar3.append(x*y)
        return ar3
            