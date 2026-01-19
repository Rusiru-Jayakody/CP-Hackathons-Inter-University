import sys
input = sys.stdin.readline
n,d,t = map(int, input().split())
heights = list(map(int, input().split()))

pref = [0] * n
suff = [0] * n
maxx = 0

for i in range(n):
    pref[i] = max(maxx, heights[i])
    maxx = pref[i]
    
maxx = 0
for i in range(n-1,-1,-1):
    suff[i] = max(maxx, heights[i])
    maxx = suff[i]
    
count = 0
for i in range(n):
    count += min(pref[i], suff[i]) - heights[i]
    
print(d*t*count)
    