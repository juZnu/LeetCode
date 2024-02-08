def minEatingSpeed( piles, h):
    min_eating = 1
    max_eating = max(piles)
    while min_eating < max_eating:
        middle = (min_eating +max_eating)//2
        total_hours = 0
        for pile in piles:
            div,mod = pile//middle,pile%middle
            if div:
                total_hours += div + (1 if mod else 0)
                continue
            total_hours += 1
        if total_hours > h:
            min_eating = middle + 1
        elif total_hours <= h:
            max_eating =middle
    return min_eating 
print(minEatingSpeed(piles = [30,11,23,4,20], h = 6))

# print(312884470//2,312884470%2)