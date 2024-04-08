from collections import deque
from typing import List


def countStudents(students: List[int], sandwiches: List[int]) -> int:
    sum1 = sum(students)
    sum0 = len(students) - sum1
    for ele in sandwiches:
        if ele and sum1:
            sum1 -= 1
        elif not ele and sum0:
            sum0 -= 1
        else:
            return sum0 + sum1
    return 0


print(countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))
