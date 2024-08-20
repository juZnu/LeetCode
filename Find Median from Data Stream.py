import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap for the lower half (invert the values to simulate max-heap using heapq)
        self.frontHeap = []
        # Min-heap for the upper half
        self.backHeap = []

    def addNum(self, num: int) -> None:
        # Add the number to the appropriate heap
        if not self.frontHeap or num <= -self.frontHeap[0]:
            heapq.heappush(self.frontHeap, -num)
        else:
            heapq.heappush(self.backHeap, num)
        
        # Balance the heaps if necessary
        if len(self.frontHeap) > len(self.backHeap) + 1:
            heapq.heappush(self.backHeap, -heapq.heappop(self.frontHeap))
        elif len(self.backHeap) > len(self.frontHeap):
            heapq.heappush(self.frontHeap, -heapq.heappop(self.backHeap))

    def findMedian(self) -> float:
        if len(self.frontHeap) > len(self.backHeap):
            return -self.frontHeap[0]
        else:
            return (-self.frontHeap[0] + self.backHeap[0]) / 2.0

# Testing the MedianFinder class
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())  # Should return 1.5
# obj.addNum(3)
# print(obj.findMedian())  # Should return 2