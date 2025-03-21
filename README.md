Straightforward set of solutions to problems 78 (Subsets), 90 (Subsets II), 77 (Combinations), 40 (Combination Sum II), 216 (Combination Sum III), 39 (Combination Sum), 46 (Permutations), 47 (Permutations II), and 131 (Palindrome Partitioning) using recursive backtracking.

The idea is essentially the same, mostly building upon what's introduced in problem 78, by constructing all subsets through recursion and then tweaking what we add to the global set by changing the base condition. 

This is how subsets are built:
- Add the current number to the list.
- Recurse with i (allow duplicates) or i + 1 (no duplicates).
- Backtrack by removing the last added number to explore other possibilities.

For sums, it's always a good idea to keep a separate sum parameter in the backtrack function than to call sum() in the base condition. O(backtrack's complexity) instead of O(N * backtrack's complexity).

Similarly, for duplicates, it is more efficient to sort and then to skip duplicate values at the same recursion depth in your loop to prevent duplicated answers (by checking i > start and nums[i] == nums[i - 1]) instead of using the not in function. Alternatively, creating a new set at every recursion depth works well too (this is exactly what I used for my Permutations II implementation but can be done similarly for Subsets II as well and probably others). This will be O(NlogN + backtrack's complexity) instead of O(N * backtrack's complexity)

Problem 40 has a particularly interesting prune technique where after we've sorted and skipped duplicates (similar to problem 90), unnecessary recursive calls can be caught quickly in the loop by checking if current_sum + candidates[i] > target which works since candidates is already sorted.

Permutation is different from combinations and subsets in the sense that instead of adding elements from the original list to a temporary list, we perform in-place swaps on the original list. 
