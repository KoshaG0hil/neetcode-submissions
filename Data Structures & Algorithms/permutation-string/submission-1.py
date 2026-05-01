class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        b=0
        count_str1={}
        count={}
        
        window=len(s1)
        
        if len(s1) > len(s2):
            return False
    
        for c in s1:
            count_str1[c]=count_str1.get(c,0)+1
        
        for c in range(window):
            count[s2[c]]=count.get(s2[c],0)+1
        
        if count==count_str1:
            return True
        
        for c in range(window,len(s2)):
            count[s2[c]]=count.get(s2[c],0)+1
            b=s2[c-window]
            count[b]-=1
            if count[b] == 0:                         # delete if zero
                del count[b]
            if count == count_str1:                   # check match
                return True
        return False
               


