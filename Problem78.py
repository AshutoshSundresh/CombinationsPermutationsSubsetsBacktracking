class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution_list = list()

        def backtrack(start, recursion_list):
            solution_list.append(recursion_list[:])

            for i in range(start, len(nums)):
                recursion_list.append(nums[i])
                backtrack(i + 1, recursion_list)
                recursion_list.pop()

        backtrack(0, [])
        return solution_list