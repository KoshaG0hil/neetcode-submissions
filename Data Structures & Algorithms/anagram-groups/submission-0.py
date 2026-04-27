class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for str in strs:
            key = "".join(sorted(str))
            if key in dictionary:
                dictionary[key].append(str)
            else:
                dictionary[key] = [str]
        
        return list(dictionary.values())