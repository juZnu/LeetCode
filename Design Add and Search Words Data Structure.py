class Node:
    def __init__(self):
        self.childrens = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        copy = self.head
        for ele in word:
            if ele not in copy.childrens:
                copy.childrens[ele] = Node()
            copy = copy.childrens[ele]
        copy.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.isEnd
            if word[i] =='.':
                for ele in node.childrens:
                    if dfs(node.childrens[ele],i+1):
                        return True
                return False
            else:
                if word[i] in node.childrens:
                    return dfs(node.childrens[word[i]],i+1)
                else:
                    return False
        return dfs(self.head,0)


# Sequence of operations
operations = ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
# Arguments for each operation
arguments = [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

wordDictionary = WordDictionary()  # Initialize the WordDictionary object.

results = []
for operation, argument in zip(operations[1:], arguments[1:]):  # Skip the first 'WordDictionary' operation for initialization.
    if operation == "addWord":
        wordDictionary.addWord(argument[0])
        results.append(None)  # addWord does not return a value.
    elif operation == "search":
        result = wordDictionary.search(argument[0])
        results.append(result)

print(results)
# Expected output: [None, None, None, False, True, True, True]
# Explanation:
# - The first three operations do not return a value as they are just adding words to the dictionary.
# - "search('pad')" should return False because "pad" was not added to the dictionary.
# - "search('bad
