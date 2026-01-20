import sys
input = sys.stdin.readline
n = int(input())
words = []
for _ in range(n):
    word = input().strip()
    words.append(word)
target = input().strip()

max_l = 0
m = len(target)
valid_prefixes = set()
for word in words:
    prefix = ""
    for c in word:
        prefix += c
        valid_prefixes.add(prefix)
        max_l = max(max_l, len(prefix))
        
dp = [float('inf')] * (m + 1)
dp[0] = 0

for i in range(1,m+1):
    for j in range(1, min(i,max_l)+1):
        s = target[i-j:i]
        if s in valid_prefixes and dp[i-j] != float('inf'):
            dp[i] = min(dp[i], dp[i-j]+1)
            
print(dp[m] if dp[m] != float('inf') else -1)
        

#We can find a more optima solution using a TRIE. will add it later