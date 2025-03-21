class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solution_list = list()
        candidates = range(1, n + 1)

        def backtrack(start, recursive_list):
            if len(recursive_list) == k:
                solution_list.append(recursive_list[:])
                return
            for i in range(start, n):
                recursive_list.append(candidates[i])
                backtrack(i + 1, recursive_list)
                recursive_list.pop()
            
        backtrack(0, [])
        return solution_list    

        