class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        m=len(matrix)   
        n=len(matrix[0])
        t=m*n

        l=0
        hi=t-1
        while l <= hi:
            m=(l+hi)//2
            row= m //n
            col= m % n
            mid_num=matrix[row][col]

            if mid_num == target:
                return True

            elif mid_num < target:
                 l= m+1
            
            else:
                hi=m-1

        return False


        








