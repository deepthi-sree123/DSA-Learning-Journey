# Password Validator

## Problem
Check if a password is valid based on the following conditions:
- Length between 8 and 12
- Contains at least one lowercase letter
- Contains at least one uppercase letter
- Contains at least one digit

```
Input:  "Abcdef123"
Output: True
```

---

## Approach
**Technique Used:** String Traversal

- Traverse string once
- Track lowercase, uppercase, digit

---

## Code (Python)

```python
def is_valid_password(password: str) -> bool:
    if len(password) < 8 or len(password) > 12:
        return False

    lower = upper = digit = False

    for ch in password:
        if ch.islower():
            lower = True
        elif ch.isupper():
            upper = True
        elif ch.isdigit():
            digit = True

    return lower and upper and digit

print(is_valid_password("Abcdef123"))
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
