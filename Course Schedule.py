from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj= {i:[] for i in range(numCourses)}
        for course1,course2 in prerequisites:
            adj[course1].append(course2)
        memo ={}

        def dfs(node,visited):
            if node in memo:return memo[node]
            if node in visited:return False

            visited.add(node)
            prev = True

            for neigh in adj[node]:
                prev = prev and dfs(neigh,visited)

            visited.remove(node)
            memo[node] = prev
            return prev
        
        res = True
        for node in range(numCourses):
            res = res and dfs(node,set())

        return res