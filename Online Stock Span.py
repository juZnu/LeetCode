class StockSpanner:

    def __init__(self):
        self.queue = []

    def next(self, price: int) -> int:
        span = 1
        
        while self.queue and self.queue[-1][0] <= price:
            price_back,span_back = self.queue.pop()
            span += span_back

        self.queue.append((price,span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)