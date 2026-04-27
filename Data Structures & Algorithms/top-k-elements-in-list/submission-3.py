class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1 - count frequencies
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] = dictionary[num] + 1
            else:
                dictionary[num] = 1
        
        # Step 2 - convert to list
        newlist = list(dictionary.items())
        
        # Step 3 - sort by frequency
        sorted_list = sorted(newlist, key=lambda x: x[1], reverse=True)
        
        # Step 4 - pick top k
        result = []
        for i in range(k):
            result.append(sorted_list[i][0])
        
        return result  #  inside function now!