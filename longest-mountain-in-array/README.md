LONGEST MOUNTAIN IN ARRAY - DIFFICULTY: MEDIUM

strategy:
- (WORSE) two pointers starting from left with states (up/down)
- (BETTER) find peak and expand from there (left and right)

TAKEAWAYS:
- careful with too many states. Hard to debug
- Safe bounds: Prevent index out of bound error

Complexity:
- Time: O(N)
- Space: O(1)
