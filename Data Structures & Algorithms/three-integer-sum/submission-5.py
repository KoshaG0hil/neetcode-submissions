class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]                          # 8 spaces
        
        nums.sort()                        # 8 spaces
        for i in range(len(nums)-2):  
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l=i+1                          # 12 spaces
            r=len(nums)-1                  # 12 spaces
            while l < r:                   # 12 spaces
                if nums[i]+nums[l]+nums[r] > 0:    # 16 spaces
                    r=r-1                          # 20 spaces
                elif nums[i]+nums[l]+nums[r] < 0:  # 16 spaces
                    l=l+1                          # 20 spaces
                else:                              # 16 spaces
                    result.append([nums[i],nums[l],nums[r]])  # 20 spaces
                    while l < r and nums[l] == nums[l+1]:   # check next l
                        l=l+1
                    while l < r and nums[r] == nums[r-1]:   # check next r
                        r=r-1  
                    l=l+1
                    r=r-1
        return result                      # 8 spaces