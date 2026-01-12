DIFFICULTY: EASY

"No same element twice" → Need to track indices, not values.
"Exactly one solution" → No need to handle multiple pairs.

Brute force checking all pairs, can do better ? -> using hash map

```nums[i] + nums[j] == target``` -> ```complement = target - num``` and store in hashmap

