class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderGraph ={ c : i for i, c in enumerate(order)}

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j == len(words[i+1]):
                    return False
                char1,char2 = words[i][j],words[i+1][j]

                if char1 == char2:continue
                else:
                    if orderGraph[char1] > orderGraph[char2]:
                        return False
                    break
        return True
            

        