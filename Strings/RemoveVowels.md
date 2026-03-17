# Remove Vowels from a String

## Problem
Remove all vowels from a given string.

```
Input:  "Deepthi Sree"
Output: "Dpth Sr"
```

---

## Code (Python)

```python
def remove_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""

    for ch in s:
        if ch not in vowels:
            result += ch

    return result

print(remove_vowels("Deepthi Sree"))
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
