# 📌 Problem: Trapping Rain Water

* LeetCode #: 42
* Approach: Prefix Max Arrays

---

## 🧠 Intuition

Water trapped at each index depends on:
- Left maximum height
- Right maximum height

Water at index =  
`min(leftMax, rightMax) - height[i]`

---

## ⚙️ Approach

1. Create `maxleft` array → stores max till index from left
2. Create `maxright` array → stores max till index from right
3. For each index:
   - Calculate water = min(maxleft, maxright) - height[i]
   - Add to total

---

## 💻 Code (Python)

```python
class Solution:
    def trap(self, height):
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n

        maxleft[0] = height[0]
        maxright[n-1] = height[n-1]

        # fill maxleft
        for i in range(1, n):
            maxleft[i] = max(maxleft[i-1], height[i])

        # fill maxright
        for i in range(n-2, -1, -1):
            maxright[i] = max(maxright[i+1], height[i])

        waterTrapped = 0

        # calculate water
        for i in range(n):
            waterTrapped += min(maxleft[i], maxright[i]) - height[i]

        return waterTrapped
