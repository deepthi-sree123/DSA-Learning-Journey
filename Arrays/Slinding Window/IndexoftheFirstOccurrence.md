# 📌 Problem: Find the Index of the First Occurrence in a String

* LeetCode #: 28
* Approach: Brute Force (Sliding Window)

---

## 🧠 Intuition

We need to find where `needle` first appears in `haystack`.

👉 Slide a window of size `len(needle)`  
👉 Compare substring with `needle`

---

## ⚙️ Approach

1. Loop from `0 → len(haystack) - len(needle)`
2. At each index:
   - Extract substring of length `needle`
   - Compare with `needle`
3. If match → return index
4. If not found → return -1

---

## 💻 Code (Python)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1

```
```python
# 🧪 Dry Run: Find the Index of the First Occurrence in a String

---

## 🔍 Example 1

haystack = "sadbutsad"  
needle = "sad"

### Step-by-step:

- i = 0  
  substring = haystack[0:3] = "sad" ✅ match  
  👉 return 0

---

## 🔍 Example 2

haystack = "leetcode"  
needle = "leeto"

### Step-by-step:

- i = 0  
  substring = "leetc" ❌  
- i = 1  
  substring = "eetco" ❌  
- i = 2  
  substring = "etcod" ❌  
- i = 3  
  substring = "tcode" ❌  

👉 No match found → return -1

---

## 🔍 Example 3

haystack = "hello"  
needle = "ll"

### Step-by-step:

- i = 0  
  substring = "he" ❌  
- i = 1  
  substring = "el" ❌  
- i = 2  
  substring = "ll" ✅ match  
  👉 return 2

---

## 📝 Key Understanding

* We check every possible window of size `len(needle)`
* As soon as we find match → stop
* If loop ends → no match

---
