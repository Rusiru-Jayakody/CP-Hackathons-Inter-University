import sys
from collections import Counter
input = sys.stdin.readline
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

c1 = Counter(l1)
c2 = Counter(l2)
ans = []

for k,v in c1.items():
    if k in c2:
        for _ in range(min(v,c2[k])):
            ans.append(k)
ans.sort()

if len(ans) == 0:
    print("NONE")
else:
    print(" ".join(map(str,ans)))
    