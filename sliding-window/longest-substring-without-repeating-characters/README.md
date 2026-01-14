DIFFICULTY: MEDIUM

Longest contiguous sequence -> sliding window

First approach: Check all substrings -> O(n2)
Better approach: Use a hashmap to store last seen chars, when a duplicate is found move left pointer