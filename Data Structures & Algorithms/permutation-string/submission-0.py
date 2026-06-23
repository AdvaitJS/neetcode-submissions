class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        chr_dict = defaultdict(int)
        freq_window = defaultdict(int)
        left , right = 0 , 0 
        
        for i in s1:
            chr_dict[i] = chr_dict[i]+1
        
        while right < len(s2):
            freq_window[s2[right]] = freq_window[s2[right]] +1 

            

            
            
            if right - left + 1 == len(s1):
                if (freq_window == chr_dict): 
                    return True
                    
                
                freq_window[s2[left]] = freq_window[s2[left]] - 1 
                if freq_window[s2[left]] == 0: freq_window.pop(s2[left])
                left +=1 
            
            right +=1
            


        return False