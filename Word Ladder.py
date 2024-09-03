class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        characters = "abcdefghijklmnopqrstuvwxyz"
        beginSet = {beginWord}
        dist = 1
        endSet = {endWord}
        while beginSet and endSet:
            wordList -= beginSet
            dist += 1
            newSet = set()

            for word in beginSet:
                for i in range(len(word)):
                    for char in characters:
                        newWord = word[:i] + char + word[i+1:]
                        if newWord in wordList:
                            if newWord in endSet:
                                return dist
                            newSet.add(newWord)
            
            if len(beginSet) > len(endSet):
                beginSet = endSet
                beginSet = newSet
            else:
                beginSet = newSet


        return 0

        

        
        