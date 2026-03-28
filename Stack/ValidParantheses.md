# Valid Parentheses (LeetCode 20)

## Problem
Check if the given string of parentheses is valid.

``` 
Input:  "()[]{}"
Output: True

Input:  "(]"
Output: False
```

---

## Approach
**Technique Used:** Stack

- Push opening brackets into stack
- For closing bracket:
  - Pop from stack
  - Check if it matches
- If stack is empty at end → valid

---

## Code (Python)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesisDict = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in paranthesisDict:
                topElement = stack.pop() if stack else '#'
                if paranthesisDict[i] != topElement:
                    return False
            else:
                stack.append(i)

        return not stack
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
