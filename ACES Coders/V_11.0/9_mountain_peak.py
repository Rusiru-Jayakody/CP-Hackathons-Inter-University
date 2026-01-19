import sys
input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))

ans = [-1] * n
stk = []
for i in range(n-1,-1,-1):
    curr = heights[i]
    while stk and stk[-1] <= curr:
        stk.pop()
    if stk:
        ans[i] = stk[-1]
    stk.append(heights[i])
print(" ".join(map(str, ans)))
    
    
    