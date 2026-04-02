Two pointers is a very common DSA technique used mainly with arrays and strings.
Instead of using one index, we use two indices (pointers) to solve problems efficiently.

1. Concept

Two pointers means using two variables that point to different positions in the array.
Example:
arr = [1,2,3,4,5]
left  → start of array
right → end of array
Index: 0 1 2 3 4
Array: 1 2 3 4 5
       ↑       ↑
      left   right

These pointers move depending on conditions.

2.Types of Two Pointer Patterns

Pattern 1 — Opposite Direction Pointers
Pointers start at both ends.

left  → start
right → end

Used in:
Reverse array
Palindrome check
Container with most water

Example:
[1,2,3,4,5]
 ↑       ↑
 L       R

Pattern 2 — Same Direction Pointers
Both pointers move from left to right.

slow pointer
fast pointer

Used in:
remove duplicates
move zeros
partition problems

Example:
[1,1,2,2,3]

slow → unique elements
fast → scanning elements
