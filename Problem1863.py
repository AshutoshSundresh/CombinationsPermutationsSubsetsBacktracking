class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets_list = list()

        def backtrack(start, recursion_list):
            subsets_list.append(recursion_list[:])

            for i in range(start, len(nums)):
                recursion_list.append(nums[i])
                backtrack(i + 1, recursion_list)
                recursion_list.pop()
        
        backtrack(0, [])

        total = 0
        for subset in subsets_list:
            subset_XOR_total = 0
            for num in subset:
                subset_XOR_total ^= num
            total += subset_XOR_total
        
        return total
