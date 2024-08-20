class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        graph = collections.defaultdict(set)

        for string in allowed:
            graph[string[:2]].add(string[2])
        
        memo ={}
        def construct(prevBlock,nextBlock,i):
            if (prevBlock,nextBlock) in memo:
                return memo[(prevBlock,nextBlock)]
                
            if len(prevBlock) == 1:
                return True

            if i == len(prevBlock)-1:
                return construct(nextBlock,'',0)

            False

            for char in graph[prevBlock[i:i+2]]:
                if construct(prevBlock,nextBlock+char,i+1):
                    memo[(prevBlock,nextBlock)] = True
                    return True
            
            memo[(prevBlock,nextBlock)] = False

            return False

        return construct(bottom,'',0)