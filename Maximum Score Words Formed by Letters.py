class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        hashmap = Counter(letters)
        words = [(word, sum([score[ord(char) - ord('a')] for char in word])) for word in words]
        res = [0]
        def backTracking(i,hashmap,carry_score):
            if i == len(words):
                res[0] = max(res[0],carry_score)
                return
            backTracking(i+1,hashmap,carry_score)
            present = True
            copyHashmap = hashmap.copy()
            word_i,word_score = words[i]
            for ele in word_i:
                if not copyHashmap.get(ele,0):
                    present = False
                    break
                copyHashmap[ele] -= 1
            if present:
                backTracking(i+1,copyHashmap,carry_score+word_score)
        
        backTracking(0,hashmap,0)

        return res[0]