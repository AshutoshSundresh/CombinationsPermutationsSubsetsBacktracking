class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution_list = []
        nums.sort()

        def backtrack(start, recursive_list):
            solution_list.append(recursive_list[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                recursive_list.append(nums[i])
                backtrack(i + 1, recursive_list)
                recursive_list.pop()

        backtrack(0, [])
        return solution_list    