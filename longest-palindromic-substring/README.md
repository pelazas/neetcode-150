# Problem: Longest Palindromic Substring - DIFFICULTY: MEDIUM

## 1. The Approach

### Expand Around Center
Instead of finding the start and end of a palindrome, iterate through the string and assume every character (or gap between characters) is the center of a palindrome. Expand outwards left and right as long as the characters match.
* **Complexity:** $O(n^2)$ Time, $O(1)$ Space.

---

## 2. Key Insights for the Solution

### 1. Two Types of Centers
A palindrome can be odd or even in length. Most people forget the even case.
* **Odd Length:** The center is a specific character (e.g., "aba", center is 'b').
    * Expand from `(i, i)`.
* **Even Length:** The center is the space *between* two characters (e.g., "abba", center is between 'b' and 'b').
    * Expand from `(i, i+1)`.

**Strategy:** For every index `i`, run both expansions and take the maximum length.


### 2. The Helper Function (`expandFromCenter`)
A helper function simplifies the code significantly.
* It takes `left` and `right` indices.
* While valid (`left >= 0`, `right < len`) and matching (`s[left] == s[right]`):
    * Move `left` back (`-1`).
    * Move `right` forward (`+1`).
* **Return Length:** `right - left - 1`.
    * *Why -1?* Because the loop breaks when the indices are already **one step too far** (invalid).

### 3. Calculating the Start Index
When we find a new `max_len`, we need to figure out where that substring starts based on the center `i`.
* **Formula:** `start = i - (len - 1) // 2`
* This integer division works correctly for both odd and even lengths.

---
