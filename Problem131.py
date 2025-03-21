class Solution:
    def partition(self, s: str) -> List[List[str]]:
        solution_list = []

        def backtrack(start, recursive_list):
            if start == len(s): 
                solution_list.append(recursive_list[:])
                return
            
            for end in range(start, len(s)):
                substring = s[start:end + 1]  
                if substring == substring[::-1]: 
                    recursive_list.append(substring)
                    backtrack(end + 1, recursive_list)
                    recursive_list.pop()  

        backtrack(0, [])
        return solution_list
