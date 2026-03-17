# Reverse Words in a String

## Problem
Reverse the order of words in a string.

```
Input:  "the sky is blue"
Output: "blue is sky the"
```

---

## Code (Python)

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
```

---

## Time Complexity
```
O(n)
```

## Space Complexity
```
O(n)
```
