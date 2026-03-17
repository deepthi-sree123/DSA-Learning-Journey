# Replace Vowels in a String

## Problem
Replace all vowels in a string with `*`.

```
Input:  "Deepthi Sree"
Output: "D**pth* Sr**"
```

---

## Code (Python)

```python
def replace_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""

    for ch in s:
        if ch in vowels:
            result += "*"
        else:
            result += ch

    return result

print(replace_vowels("Deepthi Sree"))
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
