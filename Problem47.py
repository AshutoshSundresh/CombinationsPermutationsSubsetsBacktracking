class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        solution_list = list()

        def backtrack(start):
            if len(nums) == start:
                solution_list.append(nums[:])
                return
            
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue  
                
                seen.add(nums[i]) 
                
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return solution_list

        