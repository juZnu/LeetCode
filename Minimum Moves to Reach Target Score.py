def minMoves( target: int, maxDoubles: int) -> int:
    if not maxDoubles: return target-1
    if target == 1: return 0

    if target % 2 == 0:
        return 1 + self.minMoves(target // 2, maxDoubles - 1)
    else:
        return 1 + self.minMoves(target - 1, maxDoubles)


print(minMoves(10,4))