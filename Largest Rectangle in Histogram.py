def largestRectangleArea(heights):
    maxArea = 0
    stack = []  # pair: (index, height)
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            carryarea = height * (i - index)
            maxArea = max(maxArea, carryarea)
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea
print(largestRectangleArea(heights = [2,1,5,6,2,3]))
print(largestRectangleArea(heights = [5,4,1,2]))