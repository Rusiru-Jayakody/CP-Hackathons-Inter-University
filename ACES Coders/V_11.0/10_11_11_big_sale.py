import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    prices = list(map(int, input().split()))
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(1,n+1):
        limit = min(i,m)
        for j in range(1,limit + 1):
            total = prices[j-1]
            if dp[i-j] != float('inf'):
                curr_total = total + dp[i-j]
                dp[i] = min(dp[i], curr_total)
    print(dp[n])


#This solution is accepted in pypy3.
    