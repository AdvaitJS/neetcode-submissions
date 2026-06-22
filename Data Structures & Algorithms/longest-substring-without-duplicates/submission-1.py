class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right , left =  0 , 0 
        
        answer = 0 
        seen = set()
        while right < len(s):

            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            

            
            
        
            answer = max(answer , right-left+1)
            


            right +=1
        return answer