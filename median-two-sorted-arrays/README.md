# Problem: Median of Two Sorted Arrays

## 1. The Complexity Hint: O(log n)
Whenever a problem description explicitly asks for a time complexity of **O(log n)** (or similar, like O(log(m+n))), it is a massive hint to use **Binary Search**.

* **Linear Time O(n):** Looking at every element once.
* **Logarithmic Time O(log n):** Discarding half of the remaining elements at every step.

Since the input arrays are already **sorted**, we don't need to look at every element. We can use Binary Search to "jump" to the correct answer by narrowing down the search space by half in each iteration.

---

## 2. The Brute Force Approach
The most intuitive way to solve this is to simply merge the lists.

**Algorithm:**
1.  Create a new array `merged`.
2.  Iterate through both `nums1` and `nums2`, adding the smaller element to `merged` (Two Pointers technique).
3.  Once merged, calculate the median based on the middle index.

**Why it is not optimal:**
* **Time Complexity:** $O(m + n)$. We touch every element. This fails the specific $O(\log (m+n))$ requirement.
* **Space Complexity:** $O(m + n)$. We create a new array to hold the data.

---

## 3. The Optimal Solution: Partitioning

Instead of merging, we try to find a **Partition Line** (or "Cut") that splits both arrays into two halves: a **Left Half** (containing the smaller numbers) and a **Right Half** (containing the larger numbers).

### A. How to Split (The "Cut")
We only need to Binary Search on the **smaller array** (`A`).
If we decide to cut `A` at index `i`, the cut for `B` (index `j`) is calculated automatically to ensure the Left Half has exactly half the total elements.

* **Total Elements:** `total = m + n`
* **Left Half Size:** `half = (total + 1) // 2` (The `+1` ensures that if the total is Odd, the extra element goes to the Left).
* **The Formula:** `j = half - i`

### B. How to Check if Correct (The "Cross Check")
For a partition to be valid, all elements on the Left must be smaller than all elements on the Right. Since the individual arrays are already sorted, we only need to check the boundaries (the "Cross"):

1.  Is `A_left` ≤ `B_right`?
2.  Is `B_left` ≤ `A_right`?

*Note: If a partition is at the start (index 0), use `-infinity` for Left. If at the end (index length), use `+infinity` for Right.*

### C. How to Adjust the Cut
If the Cross Check fails, we use Binary Search logic to adjust the cut on `A`:

* **If `A_left > B_right`:**
    * The numbers we picked from `A` are too big to be in the Left Half.
    * **Action:** Move Left (`high = cut_A - 1`).
* **If `B_left > A_right`:**
    * The numbers we picked from `A` are too small (meaning `B`'s numbers are too big and encroaching). We need *more* from `A`.
    * **Action:** Move Right (`low = cut_A + 1`).

### D. How to Get the Median
Once the correct partition is found:

* **Odd Total Length:**
    The median is the largest element in the Left Half.
    `Median = max(A_left, B_left)`

* **Even Total Length:**
    The median is the average of the largest Left element and the smallest Right element.
    `Median = (max(A_left, B_left) + min(A_right, B_right)) / 2`
