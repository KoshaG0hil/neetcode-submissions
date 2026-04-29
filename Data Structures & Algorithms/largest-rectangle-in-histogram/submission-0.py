class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        
        stack =[]

        max_area=0

        for index,height in enumerate(heights):
            start=index

            while stack and height < stack[-1][1]:
                i,h=stack.pop()
                width=index-i
                area= h * width
                max_area=max(max_area,area)
                start=i

            stack.append((start,height))

        for index,height in stack:
            area=height * (len(heights)-index)
            max_area=max(max_area,area)
            

        return max_area










            




