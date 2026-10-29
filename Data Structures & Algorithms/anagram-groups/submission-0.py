class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        second_lst=[]
        for x in strs:
            second_lst.append(''.join(sorted(x)))
        dict_1={}
        for i in range(len(second_lst)):
            if second_lst[i] in dict_1:
                dict_1[second_lst[i]].append(strs[i])
            else:
                dict_1[second_lst[i]]=[strs[i]]
        ret_x=[]
        for key, value in dict_1.items():
            ret_x.append(value)
        return ret_x