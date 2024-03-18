def uniquePaths( m: int, n: int) -> int:
    grid  = [1 for _ in range(n)]
    for _ in range(1,m):
        prev = 0
        for i in range(len(grid)):
            grid[i] += prev
            prev = grid[i]
    return grid[-1]

print(uniquePaths(m = 3, n = 7))