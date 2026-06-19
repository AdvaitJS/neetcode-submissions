class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        for i in strs[1:]:
            x = ""
            for j in range(min(len(a) , len(i))):
                if a[j] != i[j]:
                    break
                else:
                    x+=a[j]
            a = x
        return a