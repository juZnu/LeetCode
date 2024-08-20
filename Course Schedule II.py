class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        inDegree = collections.defaultdict(int)

        for course,preq in prerequisites:
            graph[preq].append(course)
            inDegree[course] += 1
        
        queue = collections.deque()
        result = []

        for key in range(numCourses):
            if not inDegree[key]:
                queue.append(key)
                result.append(key)
            
        while queue:
            course  = queue.popleft()
            for next_course in graph[course]:
                inDegree[next_course] -= 1
                if not inDegree[next_course]:
                    queue.append(next_course)
                    result.append(next_course)

        
        return result if len(result) == numCourses else []

        