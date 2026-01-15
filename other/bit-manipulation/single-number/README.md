SINGLE NUMBER - difficulty easy

- every number appear twice except one.

bitwise xor -> ```a ^ a = 0```, ```a ^ 0 = a```

```python
4 ^ 1 ^ 2 ^ 1 ^ 2
→ (1 ^ 1) ^ (2 ^ 2) ^ 4
→ 0 ^ 0 ^ 4
→ 4
```

COMPLEXITY
- time: O(N)
- space: O(1)