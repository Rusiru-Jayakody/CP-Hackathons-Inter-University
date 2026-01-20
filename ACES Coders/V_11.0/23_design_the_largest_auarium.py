import sys
input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))

l,r = 0,n-1
maxx = 0
while l < r:
    amt = min(heights[l],heights[r])*(r-l)
    maxx = max(maxx,amt)
    if heights[l] < heights[r]:
        l += 1
    else:
        r -= 1
print(maxx)