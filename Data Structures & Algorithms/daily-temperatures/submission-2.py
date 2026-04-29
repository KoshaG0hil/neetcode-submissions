# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
          
#             n=len(temperatures)
#             answer=[0]* n   # u set all the indices to 0 in the list as of now 0 *n 

#             stack=[]

#             for i,t in enumerate(temperatures):   # for index is i and current temp is t

#                 while stack and stack[-1][0]  < t:    #stack(a,b)  b= temp is < then temp of i+1

#                     x,y= stack.pop()     # as we have use enumerate it gives tuple and have to pop with tuple u cant pop either one
#                     answer[y]=i-y         # in the list where we want to return num of days by current index - previos index we do asnwer[stack_i] to update only previous day index and
#                                                     # if u write answer[i] it will assume current i 
#                 stack.append((t,i))
#             return answer



class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result