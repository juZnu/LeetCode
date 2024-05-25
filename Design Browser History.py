class Node:
    def __init__(self,url,prev= None,next= None):
        self.url = url
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

        
    def visit(self, url: str) -> None:
        self.current.next = Node(url,self.current)
        self.current  = self.current.next

    def back(self, steps: int) -> str:
        i =0
        while self.current.prev and i < steps:
            self. current = self. current.prev
            i += 1
        return self.current.url

    def forward(self, steps: int) -> str:
        i =0
        while self.current.next and i < steps:
            self.current = self.current.next
            i += 1
        return self.current.url

        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)