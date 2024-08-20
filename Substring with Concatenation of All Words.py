from collections import Counter


def findSubstring( s, words):
    
    starting_words = set([ele[0] for ele in words])
    lengthWord = len(words[0])
    length = len(words) * lengthWord
    wordsSet = set(words)
    hashWords = 0
    for word in words:
        hashWords += hash(word)
    res = []
    for i in range(len(s)-length+1):
        if s[i] in starting_words and s[i:i+lengthWord] in wordsSet:
            hashCarry = 0
            j = i
            for _ in words:
                p = s[j:j+lengthWord]
                hashCarry += hash(s[j:j+lengthWord]) 
                j += lengthWord
            if hashCarry == hashWords:
                res.append(i)
    return res
            


print(findSubstring(s = "wordgoodgoodgoodbestword" ,words = ["word","good","best","good"]))
        