from typing import List


def replaceWords(dictionary: List[str], sentence: str) -> str:
    head = {}
    for word in dictionary:
        hashmap = head
        for i in range(len(word)):
            if word[i] not in hashmap:
                hashmap[word[i]] = ({},True if i == len(word)-1 else False)
            hashmap = hashmap[word[i]][0]   
    result = []

    for word in sentence.split(' '):
        hashmap = head
        for i in range(len(word)):
            if word[i] in hashmap:
                hashmap,isEnd = hashmap[word[i]] 
                if isEnd:
                    result.append(word[:i+1])
                    break
            else:
                result.append(word)
                break
            
            
    return ' '.join(result)
print(replaceWords(dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))