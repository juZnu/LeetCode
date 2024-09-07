def trap( height):
    if len(height) < 2 :return 0

    i = 0
    j = 0
    contain = 0

    while j < len(height):
        if height[j] >= height[i]:
            subConatain = (j-i) * height[i]
            while i < j:
                subConatain -= height[i]
                i+= 1
            contain += subConatain
        j += 1

    return contain+trap(height[i:j][::-1])

print(trap([4,2,3]))