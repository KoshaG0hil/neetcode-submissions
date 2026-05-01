class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        from typing import List

        
        m=len(matrix)
        n=len(matrix[0])
        t= m *n      
        l=0
        hi=t-1        
        while l <= hi:
            m=(l+hi)//2         
            i= m //n  #row index
            j=m % n	#column index                       
            mid_num=matrix[i][j]
            
            if target == mid_num:
                return True           
            elif target < mid_num:
                hi= m-1                
            else:
                l=m+1
                
        return False
                  

    









