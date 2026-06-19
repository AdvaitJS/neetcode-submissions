class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l , r = 0 , len(s)-1
        for i in range(len(s)//2):
            s[r] , s[l] = s[l] , s[r]
            l+=1
            r-=1
