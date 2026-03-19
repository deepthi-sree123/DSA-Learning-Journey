# Valid Anagram

## Problem
Check if two strings are anagrams (contain same characters with same frequency).

```
Input:  s = "anagram", t = "nagaram"
Output: True

Input:  s = "rat", t = "car"
Output: False
```

---

## Approach
**Technique Used:** HashMap (Frequency Count)

- Count characters of both strings
- Compare counts

---

## Code (Python)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
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

---

## Optimized Code (HashMap)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True
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
