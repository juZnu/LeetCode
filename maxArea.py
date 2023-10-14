def maxArea(height):
    l = 0
    r = len(height)-1
    max_container = (r-l) * (height[l] if height[l]< height[r] else height[r])
    while l<r:
        if height[l] >height[r]:    
            r -= 1
        else:
            l +=1
        max_container = max(max_container,(r-l) * (height[l] if height[l]< height[r] else height[r]))
    return max_container
