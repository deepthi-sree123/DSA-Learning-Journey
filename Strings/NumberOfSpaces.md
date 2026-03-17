# Number of Spaces in a String

## Problem
Count the number of spaces in a given string.

```
Input:  "Deepthi Sree lives in Hyderabad"
Output: 4
```

---

## Code (Python)

```python
def count_spaces(text):
    count = 0
    for char in text:
        if char == " ":
            count += 1
    return count

print(count_spaces("Deepthi Sree lives in Hyderabad"))
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
