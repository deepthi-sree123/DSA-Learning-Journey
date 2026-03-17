# Longest Common Prefix (First & Last Method)

## Problem
Find the longest common prefix string among an array of strings.

```
Input:  ["flower","flow","flight"]
Output: "fl"

Input:  ["dog","racecar","car"]
Output: ""
```

---

## Idea
- Sort the array
- Compare only **first and last strings**
- Common prefix of these two = answer

---

## Code (Python)

```python
class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and first[i] == last[i]:
            i += 1
        
        return first[:i]
```

---

## Time Complexity
```
O(n log n)
```

## Space Complexity
```
O(1)
```
