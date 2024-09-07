class MaxSegmentTree:
    def __init__(self,nums) -> None:
        self.length = len(nums)
        self.nums = [0 for _ in range((2*self.length))]
        
        for i in range(self.length):
            self.nums[self.length+i] = nums[i]
            
        i = self.length-1
        while i>=0:
            self.nums[i] = max(self.nums[2*i],self.nums[(2*i)+1])
            i -= 1
    
    def update(self,index,value):
        index += self.length
        self.nums[index] = value
        while index:
            self.nums[index//2] = max(self.nums[index//2] , self.nums[index]) 
            index //= 2
    
    def range(self,start,end):
        start += self.length
        end += self.length + 1
        while start != end:
            start //= 2
            end //=2
        return self.nums[start]

    def max(self):
        return self.nums[0]

class MinSegmentTree:
    def __init__(self,nums) -> None:
        self.length = len(nums)
        self.nums = [0 for _ in range((2*self.length))]
        
        for i in range(self.length):
            self.nums[self.length+i] = nums[i]
            
        i = self.length-1
        while i>=0:
            self.nums[i] = min(self.nums[2*i],self.nums[(2*i)+1])
            i -= 1
    
    def update(self,index,value):
        index += self.length
        self.nums[index] = value
        while index:
            self.nums[index//2] = min(self.nums[index//2] , self.nums[index]) 
            index //= 2
    
    def range(self,start,end):
        start += self.length
        end += self.length 
        while start != end:
            start //= 2
            end //=2
        return self.nums[start]

    def max(self):
        return self.nums[0]

def test_max_segment_tree():
    print("Testing MaxSegmentTree")
    passed_tests = 0

    # Test Case 1: Odd length array
    nums = [2, 1, 5, 3, 4]
    max_seg_tree = MaxSegmentTree(nums)
    assert max_seg_tree.range(0, 4) == 5
    assert max_seg_tree.range(1, 3) == 5
    passed_tests += 2

    # Test Case 2: Even length array
    nums = [7, 2, 3, 1, 9, 5]
    max_seg_tree = MaxSegmentTree(nums)
    assert max_seg_tree.range(0, 5) == 9
    assert max_seg_tree.range(2, 4) == 9
    passed_tests += 2

    # Test Case 3: Array with negative values
    nums = [-2, -3, -1, -4, -5]
    max_seg_tree = MaxSegmentTree(nums)
    assert max_seg_tree.range(0, 4) == -1
    assert max_seg_tree.range(1, 3) == -1
    passed_tests += 2

    # Test Case 4: Array with mixed positive and negative values
    nums = [3, -1, 4, 1, -5, 9, -2]
    max_seg_tree = MaxSegmentTree(nums)
    assert max_seg_tree.range(0, 6) == 9
    assert max_seg_tree.range(1, 5) == 9
    passed_tests += 2

    # Test Case 5: Updates and re-check
    max_seg_tree.update(1, 10)
    assert max_seg_tree.range(0, 6) == 10
    assert max_seg_tree.range(2, 4) == 4
    passed_tests += 2

    # Test Case 6: Edge case - single element array
    nums = [10]
    single_element_tree = MaxSegmentTree(nums)
    assert single_element_tree.range(0, 0) == 10
    single_element_tree.update(0, 15)
    assert single_element_tree.range(0, 0) == 15
    passed_tests += 2

    # Test Case 7: Maximum value of the entire array
    assert max_seg_tree.max() == 10
    passed_tests += 1

    print(f"MaxSegmentTree: {passed_tests} tests passed.")


def test_min_segment_tree():
    print("Testing MinSegmentTree")
    passed_tests = 0

    # Test Case 1: Odd length array
    nums = [2, 1, 5, 3, 4]
    min_seg_tree = MinSegmentTree(nums)
    assert min_seg_tree.range(0, 4) == 1
    assert min_seg_tree.range(1, 3) == 1
    passed_tests += 2

    # Test Case 2: Even length array
    nums = [7, 2, 3, 1, 9, 5]
    min_seg_tree = MinSegmentTree(nums)
    assert min_seg_tree.range(0, 5) == 1
    assert min_seg_tree.range(2, 4) == 1
    passed_tests += 2

    # Test Case 3: Array with negative values
    nums = [-2, -3, -1, -4, -5]
    min_seg_tree = MinSegmentTree(nums)
    assert min_seg_tree.range(0, 4) == -5
    assert min_seg_tree.range(1, 3) == -4
    passed_tests += 2

    # Test Case 4: Array with mixed positive and negative values
    nums = [3, -1, 4, 1, -5, 9, -2]
    min_seg_tree = MinSegmentTree(nums)
    assert min_seg_tree.range(0, 6) == -5
    assert min_seg_tree.range(1, 5) == -5
    passed_tests += 2

    # Test Case 5: Updates and re-check
    min_seg_tree.update(1, -10)
    assert min_seg_tree.range(0, 6) == -10
    assert min_seg_tree.range(2, 4) == -5
    passed_tests += 2

    # Test Case 6: Edge case - single element array
    nums = [10]
    single_element_tree = MinSegmentTree(nums)
    assert single_element_tree.range(0, 0) == 10
    single_element_tree.update(0, 5)
    assert single_element_tree.range(0, 0) == 5
    passed_tests += 2

    # Test Case 7: Minimum value of the entire array
    assert min_seg_tree.range(0, 6) == -10
    passed_tests += 1

    print(f"MinSegmentTree: {passed_tests} tests passed.")


# Run the tests
test_max_segment_tree()
print("--------")
test_min_segment_tree()
