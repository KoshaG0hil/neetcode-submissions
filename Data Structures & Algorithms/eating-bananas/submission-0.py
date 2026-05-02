class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
    
        left =1 
        right=max(piles)
        result=right



        while left <= right:
            mid=(left+right)//2

            if self.canFinish(piles,mid,h):
                result=mid
                right=mid -1
            else:
                left=mid +1
        return result
        
    def canFinish(self,piles,speed,h):
        totalhours=0

        for pile in piles:
            totalhours+=math.ceil(float(pile)/speed)
        
        return totalhours <=h



        

