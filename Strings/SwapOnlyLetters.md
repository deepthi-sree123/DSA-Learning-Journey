# Swap Only Letters in a String

## Problem
Reverse only the alphabets in a string while keeping other characters in the same position.

``` 
Input:  "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
```

---

## Code (Python)

```python
def reverse_only_letters(s: str) -> str:
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)

print(reverse_only_letters("a-bC-dEf-ghIj"))
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
