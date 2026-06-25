class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        ans = 0
        right = max(piles)
        while left<= right:
            k =  left + ( right - left)//2
            
            
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            if hours > h:
                left = k + 1 
            elif hours <= h:
                right = k - 1
                
        return left
