# 📌 Problem: Remove All Adjacent Duplicates In String

* LeetCode #: 1047
* Approach: Stack

---

## 🧠 Intuition

When two adjacent characters are the same, they cancel each other out.

A **stack** helps simulate this:
- Push characters
- If current == top → remove (pop)

---

## ⚙️ Approach

1. Initialize an empty stack
2. Traverse the string:
   - If stack not empty AND top == current → pop
   - Else → push current
3. Join stack to form result

---

## 💻 Code (Python)

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
