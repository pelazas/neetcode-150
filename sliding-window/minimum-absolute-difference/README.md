MINIMUM ABSOLUTE DIFFERENCE - DIFFICULTY: EASY

If we don't sort the array first, we can do it in a nested loop - O(n2) time complexity.

Once we sort it calculate the difference between ith number and the following.
If the difference is smaller update min_diff and restart result array.
