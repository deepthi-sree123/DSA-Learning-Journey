# LeetCode 232 — Implement Queue Using Stacks

## Concept

Queue follows FIFO:

- First In
- First Out

Using 2 stacks:

- `stack1` → for push operation
- `stack2` → for pop and peek operation

---

# Solution

```python
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Push element into queue
    def push(self, x):
        self.stack1.append(x)

    # Remove element from queue
    def pop(self):

        # If stack2 is empty, transfer elements
        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    # Get front element
    def peek(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    # Check whether queue is empty
    def empty(self):
        return not self.stack1 and not self.stack2
```

---

# Dry Run

## Initial

```text
stack1 = []
stack2 = []
```

---

# push(1)

```python
self.stack1.append(1)
```

```text
stack1 = [1]
stack2 = []
```

---

# push(2)

```text
stack1 = [1,2]
stack2 = []
```

---

# push(3)

```text
stack1 = [1,2,3]
stack2 = []
```

---

# pop()

Condition:

```python
if not self.stack2:
```

Means:

```text
If stack2 is empty
```

So transfer elements from `stack1` to `stack2`.

---

## Transfer 1

```python
self.stack2.append(self.stack1.pop())
```

Remove top from stack1:

```text
removed = 3
```

Now:

```text
stack1 = [1,2]
stack2 = [3]
```

---

## Transfer 2

Remove:

```text
2
```

Now:

```text
stack1 = [1]
stack2 = [3,2]
```

---

## Transfer 3

Remove:

```text
1
```

Now:

```text
stack1 = []
stack2 = [3,2,1]
```

---

# Final Pop

```python
return self.stack2.pop()
```

Remove top:

```text
1
```

Now:

```text
stack2 = [3,2]
```

Output:

```text
1
```

---

# Why Does This Work?

Stacks are LIFO:

```text
1 2 3
    ↑
removed first
```

After transferring:

```text
3 2 1
    ↑
removed first
```

Oldest element (`1`) comes first.

So queue behavior (FIFO) is achieved.

---

# Important Points

## `if not self.stack2`

Means:

```python
if self.stack2 is empty
```

---

## `if not stack1 and not stack2`

Means:

```python
Both stacks are empty
```

---

# Time Complexity

## Push

```text
O(1)
```

## Pop

```text
Amortized O(1)
```

## Peek

```text
Amortized O(1)
```

## Empty

```text
O(1)
```
