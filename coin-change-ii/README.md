COIN CHANGE II - DIFFICULTY MEDIUM

Dynamic programming clues:
- How many ways something can happen
- max/min (maximum profit, minimum costs, longest path...)
- every step you have set of choices and your choice affects future limitations
- overlapping subproblems, if solved recursively, solves the same input twice.

comparison to greedy:
- greedy: make the best move now and dont look back
- dp: calculate results of all choices and pick best

Given an `amount` and an array of `coins`, find the number of **unique combinations** that sum up to the amount

**Key Distinction:** Order does **not** matter. `{1, 2}` is the same as `{2, 1}`.

Very important the order of loops combinations/permutations.

- Combinations (CORRECT APPROACH) -> Find all ways using only 1s. Then, find all ways using 1s and 2s...
- Permutations -> For amount 3, try ending with a 1. Then try ending with a 2...

Recurrence formula:
`dp[x] += dp[x - coin]`

* **Logic:** "The new ways to make amount `x` equal the existing ways PLUS the ways to make the remainder (`x - coin`) if we add this coin.