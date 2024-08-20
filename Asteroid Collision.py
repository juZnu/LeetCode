class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for ele in asteroids:
            while result and  result[-1] > 0 and ele < 0:
                if abs(ele) > result[-1]:
                    result.pop()
                elif abs(ele) == result[-1]:
                    result.pop()
                    ele = 0
                else:
                    ele = 0

            if ele:result.append(ele)

        return result
        