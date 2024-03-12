from typing import List

class MinHeap:
    def __init__(self):
        self.arr = []
        
    def insert(self,element):
        self.arr.append(element)
        self.heapifyUp(len(self.arr) - 1)

    def remove(self):
        self.arr[0],self.arr[-1] = self.arr[-1],self.arr[0]
        self.arr.pop()
        self.heapifyDown(0)
        # return minVal

    def heapifyUp(self,index):
        while index > 0:
            parentIndex = index // 2
            if self.arr[parentIndex] > self.arr[index]:
                self.arr[parentIndex] , self.arr[index] = self.arr[index] , self.arr[parentIndex]
            index = parentIndex
            self.heapifyUp(parentIndex)

    def heapifyDown(self,index):
        leftChild = (2 * index ) + 1
        rightChild = (2 * index ) + 2
        largest = index
        if leftChild < len(self.arr) and self.arr[leftChild] < self.arr[largest]:
            largest = leftChild
        if rightChild < len(self.arr) and self.arr[rightChild] < self.arr[largest]:
            largest = rightChild
        if largest != index:
            self.arr[largest] , self.arr[index] = self.arr[index] , self.arr[largest]
            self.heapifyDown(largest)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = MinHeap()
        for ele in nums:
            self.minheap.insert(ele)
        while len(self.minheap.arr) > self.k:
            self.minheap.remove()
        
    def add(self, val: int) -> int:
        kth = self.minheap.arr[0] if self.minheap.arr else float('inf')
        if kth < val :
            self.minheap.insert(val)
        while len(self.minheap.arr) > self.k:
            self.minheap.remove()
        return self.minheap.arr[0]


if __name__ == "__main__":
    actions = ["KthLargest","add","add","add","add","add"]
    values = [[2,[0]],[-1],[1],[-2],[-4],[3]]
    
    # Initialization of the KthLargest object with the first element of the values list.
    kthLargest = KthLargest(values[0][0], values[0][1])
    
    results = []
    # Iterating through the actions while skipping the first initialization action.
    for action, value in zip(actions[1:], values[1:]):
        if action == "add":
            result = kthLargest.add(value[0])
            results.append(result)
    
    print("Results of add operations: ", results)
