# String Matching in an Array (LeetCode 1408)

## Problem
Return all strings in the array that are **substrings of another string** in the array.

```
Input:  ["mass","as","hero","superhero"]
Output: ["as","hero"]
```

---

## Approach
**Technique Used:** String Matching (Brute Force)

- Compare every string with every other string
- Check if one is substring of another

---

## Code (Python)

```python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break

        return result
```

---

## Time Complexity
```
O(n^2 * k)
```

## Space Complexity
```
O(1)
```
