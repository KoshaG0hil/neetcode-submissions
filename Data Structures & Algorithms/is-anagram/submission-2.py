class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_sdict= {}
        new_tdict= {}

        if len(s)!= len(t):
            return False
         
        for char in s:
            if char in new_sdict:
                new_sdict[char] = new_sdict[char] + 1
            else:
                new_sdict[char]=1

        for char in t:
            if char in new_tdict:
                new_tdict[char] = new_tdict[char] + 1
            else:
                new_tdict[char]=1

        if new_sdict==new_tdict:
            return True

        else:
            return False
        