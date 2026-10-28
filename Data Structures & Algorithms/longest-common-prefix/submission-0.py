class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=strs[0]
        for words in strs[1:]:
            while common not in words:
                if len(common)>len(words):
                    common=common[:len(words)]
                elif len(common)<len(words):
                    words=words[:len(common)]
                else:
                    words=words[:len(words)-1]
                    common=common[:len(common)-1]
        return common