class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        pairs= sorted(zip(position,speed),reverse =True)
        stack =[]


        for i,j in pairs:
            time=(target - i)/j

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
            else:
                continue
        return len(stack)




