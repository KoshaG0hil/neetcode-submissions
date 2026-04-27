class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new_list=set(nums)
        longest=0

        for num in new_list:
            if (num-1) not in new_list:
                length =1
                while (num+length) in new_list:
                    length=length+1
                
                longest=max(length,longest)

        return longest

