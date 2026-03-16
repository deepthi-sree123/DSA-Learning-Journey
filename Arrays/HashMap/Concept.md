# HashMap (Dictionary)

A **HashMap** is a data structure that stores data in **key–value pairs**.

Each **key is unique** and maps to a specific **value**.

Example:

```
Key   → Value
a     → 1
b     → 2
c     → 3
```

---

# Python Implementation

In Python, HashMaps are implemented using **dictionaries (`dict`)**.

```python
hashmap = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

Access element

```python
print(hashmap["a"])   # 1
```

Add element

```python
hashmap["d"] = 4
```

Update element

```python
hashmap["a"] = 10
```

Delete element

```python
del hashmap["b"]
```

---

# HashMap for Counting (Most Common Use)

Used to count **frequency of elements**.

Example:

```python
s = "hello"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

Output

```
{
'h':1,
'e':1,
'l':2,
'o':1
}
```

---

# Using Counter (Shortcut)

Python provides a built-in frequency counter.

```python
from collections import Counter

s = "hello"
freq = Counter(s)

print(freq)
```

Output

```
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
```

---

# Iterating Through HashMap

Keys

```python
for key in hashmap:
    print(key)
```

Values

```python
for value in hashmap.values():
    print(value)
```

Key and Value

```python
for key, value in hashmap.items():
    print(key, value)
```

---

# Time Complexity

| Operation | Complexity |
|----------|------------|
| Insert | O(1) |
| Delete | O(1) |
| Search | O(1) |

Average case complexity is **constant time**.

---

# Common Interview Uses

- Frequency counting
- Detect duplicates
- Two Sum problem
- Group anagrams
- Character counting in strings
- Hashing based lookups

---

# Example Problem

Count characters in a string.

```python
s = "banana"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

Output

```
{
'b':1,
'a':3,
'n':2
}
```
