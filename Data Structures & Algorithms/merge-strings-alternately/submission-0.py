class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        right = 0
        left = 0
        answer = ""
        while right < len(word1) and left < len(word2):
            answer += (word1[right] + word2[left])
        
            right += 1
            left += 1
            
        if right < len(word1):
            answer += word1[right::]
            
        elif left < len(word2):
            answer += word2[left::]
        return answer