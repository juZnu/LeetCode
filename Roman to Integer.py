def romanToInt(s):
    roman ={
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    
    result = 0
    for j in range(len(s)):
        i = j-1
        carry = 0
        while i>0 and s[i] <s[j]:
            carry += roman[s[i]]
            i -= 1
        result += roman[s[j]] - carry - carry

    return result

print(romanToInt("MCMXCIV"))
    