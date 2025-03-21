class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        solution_list = []
        candidates = range(1, 10)

        def backtrack(start, current_list, current_sum):
            if current_sum == n and len(current_list) == k:
                solution_list.append(current_list[:])
                return
            if len(current_list) > k:
                return
            if current_sum > n:
                return
            
            for i in range(start, len(candidates)):
                current_list.append(candidates[i])
                backtrack(i + 1, current_list, current_sum + candidates[i])
                current_list.pop()
        
        backtrack(0, [], 0)
        return solution_list       