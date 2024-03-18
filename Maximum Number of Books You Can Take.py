from typing import List


def maximumBooks( books: List[int]) -> int:
    maximum = 0
    books = [(0,ele) for ele in books]
    carry = 0
    for i in range(len(books)-1,-1,-1):
        ele =books[i]
        carry += 

print(maximumBooks(books = [8,5,2,7,9]))