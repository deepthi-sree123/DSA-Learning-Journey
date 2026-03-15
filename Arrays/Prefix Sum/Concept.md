# Prefix Sum

## Definition
Prefix Sum is a technique used to compute cumulative sums of an array so that range sum queries can be answered efficiently.

For an array `arr`:

prefix[i] = arr[0] + arr[1] + ... + arr[i]

Each position stores the sum of all elements from the start up to that index.

---

## Example

Array

```
arr = [2, 4, 1, 5, 3]
```

Prefix Sum Array

```
prefix[0] = 2
prefix[1] = 2 + 4 = 6
prefix[2] = 6 + 1 = 7
prefix[3] = 7 + 5 = 12
prefix[4] = 12 + 3 = 15
```

Result

```
prefix = [2, 6, 7, 12, 15]
```

---

## Prefix Sum Formula

```
prefix[i] = prefix[i-1] + arr[i]
```

---

## Range Sum Query

To find the sum from index **L to R**:

```
sum(L, R) = prefix[R] - prefix[L-1]
```

Example

```
arr = [2,4,1,5,3]
Find sum(1,3)
```

```
prefix = [2,6,7,12,15]

sum(1,3) = prefix[3] - prefix[0]
         = 12 - 2
         = 10
```

---

## Python Implementation

```python
arr = [2,4,1,5,3]

prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)
```

Output

```
[2, 6, 7, 12, 15]
```

---

## Range Query Function

```python
def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    return prefix[R] - prefix[L-1]
```

---

## Time Complexity

| Operation | Complexity |
|----------|-----------|
| Build Prefix Array | O(n) |
| Range Query | O(1) |

Without prefix sum → **O(n) per query**

With prefix sum → **O(1) per query**

---

## Applications

Prefix Sum is commonly used in:

- Range sum queries
- Subarray sum problems
- Subarray sum equals k
- Maximum subarray problems
- 2D matrix sum queries

---

## Key Idea

Prefix Sum converts repeated range sum calculations from **O(n)** to **O(1)** by precomputing cumulative sums.
