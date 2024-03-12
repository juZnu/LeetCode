def kBigIndices( nums, k):
    def heapify_up(list,index):
        parent_index = index //2
        if index > 0 and list[parent_index] < list[index]:
            list[parent_index],list[index] = list[index],list[parent_index]
            heapify_up(list,parent_index)
            
    def heapify_down(list,index):
        leftchild = 2*index +1
        rightchild = 2*index+2
        largest = index
        if leftchild < len(list) and list[leftchild] > list[largest]:
            largest = leftchild
        if rightchild < len(list) and list[rightchild] > list[largest]:
            largest = rightchild
        if largest != index:
            list[largest], list[index] = list[index],list[largest]
            heapify_down(list,largest)
    
    def insert(list,value):
        list.append(value)
        heapify_up(list,len(list)-1)
        return list
    
    def remove(list):
        list[0],list[-1] = list[-1],list[0]
        ele = list.pop()
        heapify_down(list,0)
        return ele,list
    
    heap= []
    for i in range(k):
        heap = insert(heap,nums[i])
    result1 = [False for _ in range(len(nums)-k-k)]
    for i in range(k, len(nums)-k):
        carryheap = heap.copy()
        carry = i 
        while carry >= k:
            ele,carryheap = remove(carryheap)
            carry -= 1
            if ele < nums[i]:
                result1[i -k] = True
                break
        heap = insert(heap,nums[i])
    heap = []
    for i in range(len(nums)-1,len(nums)-1-k,-1):
        heap = insert(heap,nums[i])
    result2 = 0
    for i in range(len(nums)-1-k,k-1,-1):
        carryheap = heap.copy()
        carry = len(nums) -i -1
        while carry >= k and result1[i-k]:
            ele,carryheap = remove(carryheap)
            carry -= 1
            if ele < nums[i]:
                result2 += 1 if result1[i-k] else 0
                break
        heap = insert(heap,nums[i])
        
        
    return result2
print(kBigIndices(nums = [4,5,3,2,3,5,7,4], k = 1))