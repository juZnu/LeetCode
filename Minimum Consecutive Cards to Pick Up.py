from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        result = float('inf')
        hashmap = {}
        for i in range(len(cards)):
            if hashmap.get(cards[i],-1) != -1: 
                result = min(i + 1 - hashmap[cards[i]] , result)
            hashmap[cards[i]] = i
        return result if result != float('inf') else -1
        