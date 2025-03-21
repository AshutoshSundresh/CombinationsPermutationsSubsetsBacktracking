class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solution_list = []
        def backtrack(start, recursive_list, current_sum):
            if current_sum == target:
                solution_list.append(recursive_list[:])
                return
            
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                recursive_list.append(candidates[i])
                backtrack(i, recursive_list, current_sum + candidates[i])
                recursive_list.pop()

        backtrack(0, [], 0)    
        return solution_list
        