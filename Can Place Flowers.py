def canPlaceFlowers(flowerbed, n):
    i = 0
    while i <(len(flowerbed)-1) and n > 0:
        if flowerbed[i] == 0 and flowerbed[i+1] == 0:
            n -= 1
            i += 1
        if flowerbed[i] == 1:
            while i <len(flowerbed)-1 and flowerbed[i]==1:
                i += 1
        i += 1
    if n > 0  and i <(len(flowerbed)):
        if flowerbed[i-1] == 0 and flowerbed[i] == 0:
            n -= 1
    return n == 0
