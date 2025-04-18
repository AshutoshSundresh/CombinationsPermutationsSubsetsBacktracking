class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution_list = list()

        def backtrack(start):
            if len(nums) == start:
                solution_list.append(nums[:])
            
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        backtrack(0)
        return solution_list