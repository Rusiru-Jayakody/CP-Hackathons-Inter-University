import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
scores = []
points = [0] * n
for i in range(n):
    score = input().strip().split()
    scores.append(score)
    
for i in range(n):
    for j in range(i+1,n):
        if i == j:
            continue
        sum_i = sum(ord(ch) for ch in scores[i][j-1])
        sum_j = sum(ord(ch) for ch in scores[j][i])
        if sum_i == sum_j:
            points[i] += 1
            points[j] += 1
        elif sum_i > sum_j:
            points[i] += 2
        else:
            points[j] += 2
           
maxx = max(points)
ans = [i+1 for i,p in enumerate(points) if p == maxx]
ans.sort()
print(" ".join(map(str,ans)))