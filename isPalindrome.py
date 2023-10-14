def isPalindrome( s):
    i =0
    j = -1
    while i-j <len(s):
        if not s[i].isalnum():
            i += 1
            continue
        elif not s[j].isalnum():
            j -= 1
            continue
        elif s[i].lower()!= s[j].lower():
            return False
        i += 1
        j -= 1
    return True