class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            d1 = {}
            d2 = {}
            for i in range(len(s)):
                d1[s[i]] = s.count(s[i])
                d2[t[i]] = t.count(t[i])
            return d1==d2
        
        
