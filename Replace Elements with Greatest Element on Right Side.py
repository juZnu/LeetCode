def replaceElements(arr):
    result = [-1] * len(arr)
    large = arr[-1]
    index = -2
    while index >= (-1)*len(arr):
        result[index] = large
        large = large if large > arr[index] else arr[index]
        index -= 1
    return result