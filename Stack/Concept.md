# 🧠 Stack (Python) — Complete Notes

---
 
## 📌 Definition

- Stack is a **linear data structure**
- Follows **LIFO* (Last In First Out)**

Example:
Push → 1, 2, 3  
Pop → 3
 
---

## ⚙️ Implementation (Python)

```python
stack = []
```

---

## 🔧 Operations

### 1. Push

```python
stack.append(10)
stack.append(20)
```

### 2. Pop

```python
stack.pop()
```

### 3. Peek

```python
top = stack[-1]
```

### 4. Check Empty

```python
if not stack:
    print("Empty")
```

---

## ⏱️ Complexity

| Operation | Time |
|----------|------|
| push | O(1) |
| pop | O(1) |
| peek | O(1) |

---

## 🎯 When to Use Stack

Use stack when you see:

- Parentheses problems → (), {}, []
- Reversal problems
- Nested structures
- Undo / Redo
- Next Greater / Smaller element

---

## 🧩 Important Patterns

---

### 🔹 1. Valid Parentheses

```python
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            stack.append(ch)

    return not stack
```

---

### 🔹 2. Monotonic Stack (Next Greater Element)

```python
def nextGreater(nums):
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)

    return res
```

---

### 🔹 3. Reverse Using Stack

```python
s = "hello"
stack = list(s)

res = ""
while stack:
    res += stack.pop()

print(res)  # "olleh"
```

---

## ⚠️ Common Mistakes

- ❌ Pop from empty stack → IndexError  
- ❌ Accessing stack[-1] when empty  
- ❌ Forgetting `while stack` condition  
- ❌ Wrong comparison in monotonic stack  

---

## 🧠 Pattern Recognition

If problem says:

- "next greater"
- "nearest smaller"
- "valid parentheses"
- "span"
- "histogram"

👉 Use **STACK**

---

## 🔥 Must Practice Problems

### 🟢 Easy
- Valid Parentheses  
- Min Stack  

### 🟡 Medium
- Next Greater Element  
- Daily Temperatures  
- Asteroid Collision  

### 🔴 Hard
- Largest Rectangle in Histogram ⭐  
- Trapping Rain Water (stack)  

---

## 💡 Interview Tips

- Use **list as stack**
- Always check:
```python
if stack:
```
- Try solving in **one pass (O(n))**
- Use **monotonic stack for optimization**

---

## 📝 Summary

```python
# Stack = LIFO
# push → append()
# pop → pop()
# peek → stack[-1]
# Time → O(1)
```

---
