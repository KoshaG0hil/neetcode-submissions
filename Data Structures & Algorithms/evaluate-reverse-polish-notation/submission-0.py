class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack =[]

        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(int(i))       
            elif i == "+":
                a, b = stack.pop(),stack.pop()
                stack.append(a + b) 
            elif i in "*":
                a,b=stack.pop(),stack.pop()
                stack.append(a*b)
            elif i in "/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            elif i in "-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)

        return stack[0]
                            

            