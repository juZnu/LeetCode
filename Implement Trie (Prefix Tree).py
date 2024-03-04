class Node:
    def __init__(self,isEnd= False):
        self.childrens = {}
        self.isEnd = isEnd

        
class Trie:
    def __init__(self):
        self.head = Node()
        
    def insert(self, word: str) -> None:
        copy = self.head
        for letter in word:
            if letter not in copy.childrens:
                copy.childrens[letter] = Node()
            copy = copy.childrens[letter]
        copy.isEnd = True

    def search(self, word: str) -> bool:
        copy = self.head
        for letter in word:
            if not letter in copy.childrens:
                return False
            copy = copy.childrens[letter]
        return copy.isEnd

    def startsWith(self, prefix: str) -> bool:
        copy = self.head
        for letter in prefix:
            if not letter in copy.childrens:
                return False
            copy = copy.childrens[letter]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param_2 = obj.search('aple')
param_3 = obj.startsWith('app')