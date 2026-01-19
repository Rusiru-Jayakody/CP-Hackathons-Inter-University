import sys
input = sys.stdin.readline
s = input().strip()

longest = 0
l = 0
seen = set()
start = 0

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l += 1
    seen.add(s[r])
    if r-l+1 > longest:
        longest = r-l+1
        start = l

print(s[start:start+longest])
