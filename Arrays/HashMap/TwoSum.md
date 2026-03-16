# Two Sum (HashMap)

## Problem
Find indices `i` and `j` such that:


nums[i] + nums[j] = target


Example:


nums = [2,7,11,15]
target = 9

Output: [0,1]


---

## Code

```python
class Solution:
    def twoSum(self, nums, target):

        hashmap = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i
