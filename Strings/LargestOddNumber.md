# Largest Odd Number in a String

## Problem
Given a numeric string `num`, return the **largest odd-numbered substring**.

```
Input:  "52"
Output: "5"

Input:  "4206"
Output: ""

Input:  "35427"
Output: "35427"
```

---

## Code (Python)

```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""
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
