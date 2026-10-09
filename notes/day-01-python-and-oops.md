# Day 01: Python Basics, Patterns and OOPs

## Python basics
- Python is an **interpreted** language: it executes line by line.
- `input()` returns a **string** by default.
- There is no `char` datatype.

**Datatypes:** `int`, `float`, `bool`, `str`
**Collections:** `list`, `dict`, `tuple`, `set` (sequential), `range`

## Operators
| Type | Operators |
|------|-----------|
| Arithmetic | `+ - * % / // ** ` |
| Logical | `or`, `and`, `not` |
| Relational | `==  !=  >=  <=  <  >` |
| Assignment | `=` |
| Ternary | `x if cond else y` |
| Bitwise | `<<  >>  &  \|` |
| Membership | `in`, `not in` |

Bitwise AND example: `5 & 4` -> `0101 & 0100 = 0100` = 4

### Left shift `<<`
`n << k = n * 2^k`
Example: `n = 6 (110)`, `k = 3`
- 1st shift: `1100`
- 2nd shift: `11000`
- 3rd shift: `110000` = 48 = 6 * 2^3

### Right shift `>>`
`n >> k = n // 2^k`

## Conditional statements
```python
if cond:
    ...
elif cond:
    ...
else:
    ...
```

## Control statements
- `break`: breaks out of the loop
- `continue`: skips the current iteration

## Loops
- `for` and `while` loops
- **No do-while loop in Python**

```python
for i in range(start, end, step):
    ...
```

Even numbers 0 to 100:
```python
for i in range(0, 101, 2):
    print(i)
```

### Formatted strings
```python
print(f"{i} - evennum = {i}")
```
`{i}` is replaced by the value of the iterate variable.

## Prime number: optimisation levels
Count divisors of `n`; prime if the count is exactly 2.

| Level | Loop range | Idea |
|-------|-----------|------|
| L-I | `range(1, n+1)` | check every number |
| L-II | `range(2, n)` | skip 1 and n |
| L-III | `range(2, n//2 + 1)` | no divisor above n/2 |
| L-IV | `range(2, int(n**0.5) + 1)` | only up to sqrt(n) |

## Variable length arguments
```python
def print_info(*args):      # dynamic variable length
    for i in args:
        print(i)

print_info("Hello", "world", 123, 456.78)
```

## Input as a list
```python
a = list(map(int, input().split(",")))   # comma separated elements
```
Practice: 1) sum of all elements, 2) print alternate elements, 3) print list in reverse.

## Dictionaries
```python
d = {'a': 1, 'b': 2, 'c': 3}
d.keys()     # ['a', 'b', 'c']
d.values()   # [1, 2, 3]
d.items()    # [('a', 1), ('b', 2), ('c', 3)]
```

Frequency in a dict:
```python
freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1
```

## Patterns
Right-angled triangle: row `i` prints `i` stars.
```python
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
```
Square / rectangle: every row `i` runs `j` from `0` to `n-1`.

## Sliding window pattern
Given `k` (window size):
1. `i = 0`, `j = 0`
2. If the window size is not achieved yet, do `j += 1`
3. If the window size is achieved, slide: `i += 1`, `j += 1`

Repeat until `j < n`.
Example: `[2, 8, 7, 12, 14]`, `k = 2`

## OOPs: object-oriented programming
- **Encapsulation**: binding of data
- **Abstraction**: hides implementation
- **Polymorphism**: existence in many forms (same name, different forms)
  - method overloading
  - method overriding
- **Inheritance**

## Problems on this page
See `leetcode/` and `python-basics/` for solutions.
