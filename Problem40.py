class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solution_list = list()
        candidates.sort()

        def backtrack(start, recursive_list, current_sum):
            if current_sum == target:
                solution_list.append(recursive_list[:])
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if current_sum + candidates[i] > target:
                    break

                recursive_list.append(candidates[i])
                backtrack(i + 1, recursive_list, current_sum + candidates[i])
                recursive_list.pop()
        
        backtrack(0, [], 0)
        return solution_list