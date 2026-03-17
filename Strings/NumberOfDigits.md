# Number of Digits in a String

## Problem
Count the number of digits in a given string.

```
Input:  "abc123de45"
Output: 5
```

---

## Code (Python)

```python
class Solution:
    def countDigits(self, s: str) -> int:
        count = 0
        
        for ch in s:
            if ch.isdigit():
                count += 1
        
        return count
```

---

## Time Complexity
```
O(n)
```

## Space Complexity
```
O(1)
```
