COIN CHANGE - DIFFICULTY MEDIUM

given coins [c1,c2,c3] and amount, find minimum coins to reach amount.

BFS APPROACH

- each node is a tuple (step, current_count)
- store in queue nodes.
- have a set for repeated nodes
- the first time we reach ```amount``` = minimum coins (return step+1)

DYNAMIC PROGRAMMING APPROACH:

- dp[i] -> minimum n of coins to reach amount i
- dp[0] = 0
- update dp[i] iteratively


COMPLEXITY:
- BFS: -> time - O(amount*len(coins))= O(n)
       -> space - (queue and visited of amount length) = O(n)
- DP:  -> time - O(amount*len(coins))
       -> space - dp array - O(amount) = O(n)

NOTES:
- BFS: more intuitive, memory-heavy for large amount
- DP: efficient, more clean