def partitionString( s):
        charSet = set()
        count = 1
        for ele in s:
            if ele  in charSet:
                count +=1
                charSet = set()
            charSet.add(ele)
        return count
    
print(partitionString(s = "aabcaabc"))