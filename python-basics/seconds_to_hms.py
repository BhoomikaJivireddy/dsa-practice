"""Convert seconds to hours, minutes and seconds."""

n = int(input())

# Method 1: using % and //
a = n // 3600
b = (n % 3600) // 60
c = (n % 3600) % 60
print(f"{a} hr: {b} min: {c} sec")

# Method 2: subtracting what is already accounted for
a = n // 3600
b = (n - a * 3600) // 60
c = n - (3600 * a + b * 60)
print(f"{a} hr: {b} min: {c} sec")
