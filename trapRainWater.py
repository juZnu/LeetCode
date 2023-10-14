def trap( height):
    i = 0
    j =1
    contain = 0
    while j != len(height):
        if height[i] <= height[j]:
            k = i
            while k < j:
                contain += height[i] - height[k] 
                k += 1
            i = j
        j += 1
    return contain + (trap(height[i:j][::-1]) if i!= j-1 else 0)