class MagicDictionary:

    def __init__(self):
        self.hashmap = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            carry = self.hashmap

            for char in word:
                if char not in carry:
                    carry[char] = dict()
                carry = carry[char]

            carry[''] = True

    def search(self, searchWord: str) -> bool:
        def helper(word,isMagic,wordDict):
            for i in range(len(word)):
                if isMagic:
                    for char,charDict in wordDict.items():
                        if char == word[i]:
                            continue
                        if char != '' and helper(word[i+1:],False,charDict):
                            return True
                if word[i] in wordDict:
                    wordDict = wordDict[word[i]]
                else:
                    return False
            if isMagic:
                return False
            return '' in wordDict
        
        return helper(searchWord,True,self.hashmap)