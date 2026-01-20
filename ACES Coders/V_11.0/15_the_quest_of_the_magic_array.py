import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
maxx = float('-inf')
temp = 1
for i in range(1,n):
    if arr[i] - arr[i-1] == 1:
        temp += 1
    else:
        maxx = max(maxx, temp)
        temp = 1
maxx = max(temp,maxx)
print(maxx)

