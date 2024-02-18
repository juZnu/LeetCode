def minSwaps( s):
    max_count = 0
    open_count = 0
    for ele in s:
        open_count += 1 if ele == ']' else (-1)
        max_count = max(open_count,max_count) 
    return (max_count + 1)//2
print(minSwaps(s = "][]["))
print(minSwaps(s = "]]][[["))