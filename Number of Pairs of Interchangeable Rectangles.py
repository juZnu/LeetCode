def interchangeableRectangles(rectangles):
    def backSum(number):
        if number  == 1:
            return 0
        return number-1 + backSum(number-1)
    count = {}
    result = 0
    for height,width in rectangles:
        count[height/width] = count.get(height/width, 0) +1
    for v in count.values():
        if v > 1:
            result += backSum(v)
    return result
    
print(interchangeableRectangles(rectangles = [[4,5],[7,8]]))