class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = popped[::-1]
        array = []
        pushed = pushed[::-1]

        while pushed and popped:
            array.append(pushed.pop())
            while array and popped and popped[-1] == array[-1]:
                popped.pop()
                array.pop()

        return not popped