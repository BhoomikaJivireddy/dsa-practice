"""Codeforces 750A: New Year and Hurry
Verdict: Accepted (Python 3, 62 ms) on Oct 06, 2026, submission 393353315.

The contest lasts 240 minutes and getting to the party takes k minutes,
so only 240 - k minutes are available. Problem i takes 5 * i minutes.
Solve problems in order and count how many fit.

NOTE: this is a reference solution. Replace it with your own accepted
submission code if you want the repo to hold exactly what you submitted.
"""

n, k = map(int, input().split())

available = 240 - k
solved = 0
used = 0

for i in range(1, n + 1):
    used += 5 * i
    if used > available:
        break
    solved += 1

print(solved)
