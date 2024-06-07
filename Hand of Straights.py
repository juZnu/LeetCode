from typing import List
import collections

def isNStraightHand( hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hashmap = collections.Counter(hand)
        for ele in hand:
            if hashmap[ele]>0:
                for i in range(groupSize):
                    if hashmap[ele+i] > 0:
                        hashmap[ele+i] -= 1
                    else:
                        return False
        return True
        
print(isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))