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
