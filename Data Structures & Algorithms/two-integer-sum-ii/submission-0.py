class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        l=0
        r=len(numbers)-1
        sum=0

        while l < r:
            sum = numbers[l]+numbers[r]
            if sum < target:
                l= l + 1
            elif sum > target:  
                r = r - 1
            
            else:               # found it!
                return [l+1, r+1]  # +1 because 1-indexed!
            
        return[]

    