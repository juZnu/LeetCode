class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(set)
        inDegree = collections.defaultdict(int)
        for recipe,ingredient in zip(recipes,ingredients):
            for ing in ingredient:
                graph[ing].add(recipe)
                inDegree[recipe] += 1
        
        queue = collections.deque()

        for supply in supplies:
            queue.append(supply)
        
        while queue:
            ing = queue.popleft()
            for value in graph[ing]:
                inDegree[value] -= 1
                if  not inDegree[value]:
                    queue.append(value)
        
        res = []
        for recipe in recipes:
            if not inDegree[recipe]:
                res.append(recipe)

        return res

        