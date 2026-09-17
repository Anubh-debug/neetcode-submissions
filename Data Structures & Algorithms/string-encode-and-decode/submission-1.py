class Solution:

    def encode(self, strs: List[str]) -> str:
        x=""
        for string in strs:
            len_str=len(string)
            y=str(len_str)+"#"+string
            x+=y
        return x
    def decode(self, s: str) -> List[str]:
        decode_list=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            starting=int(s[i:j])
            decode_list.append(s[j+1:j+1+starting])
            i=j+1+starting
        return decode_list
