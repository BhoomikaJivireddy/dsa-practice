"""Right-angled triangle star pattern.

Row i (1-indexed) prints i stars.
"""

n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
