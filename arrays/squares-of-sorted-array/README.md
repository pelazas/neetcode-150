SQUARES OF SORTED ARRAY - DIFFICULTY: EASY


first approach: square them and do nums.sort()
- nums.sort() has time complexity O(nlogn) CAN DO BETTER

key:
realize is v-shape from negatives to positives. Find index of first positive. Create two arrays, process and merge onto one
- Time complexity O(n)
- Space complexity O(n)

