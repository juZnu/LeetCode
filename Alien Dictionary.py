class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char:set() for word in words for char in word}
        inDegree = {char:0 for char in adj}

        for j in range(1,len(words)):
            word = words[j]
            prevWord = words[j-1]
            minLen = min(len(prevWord),len(word))
            if len(prevWord) > len(word) and prevWord[:minLen] == word[:minLen]:
                return ""
            for i in range(minLen):
                if word[i] != prevWord[i]:
                    if word[i] not in  adj[prevWord[i]]:
                        adj[prevWord[i]].add(word[i])
                        inDegree[word[i]] += 1
                    break
                    

        queue = collections.deque([char for char in adj.keys() if not inDegree[char]])

        res = []

        while queue:
            char = queue.popleft()
            res.append(char)
            for nextChar in adj[char]:
                inDegree[nextChar] -= 1
                if not inDegree[nextChar]:
                    queue.append(nextChar)

        return ''.join(res) if len(res)== len(adj) else ''


                
                


