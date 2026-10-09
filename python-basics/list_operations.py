"""Basic list operations on comma separated input, e.g. 1,2,3,4."""

a = list(map(int, input().split(",")))

# 1. sum of all elements
print(sum(a))

# 2. alternate elements
print(a[::2])

# 3. list in reverse
print(a[::-1])
