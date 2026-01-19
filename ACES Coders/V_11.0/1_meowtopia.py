import sys
input = sys.stdin.readline
n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

visited = [False] * n
def dfs(u):
    visited[u] = True
    for v in range(n):
        if grid[u][v] == 1 and not visited[v]:
            dfs(v)
    return

#intead od dfs we can use bfs for the solution
# from collecton import deque
# def bfs(u):
#     q = deque([u])
#     visited[u] = True
#     while q:
#         node = q.popleft()
#         for i in range(n):
#             if grid[node][i] == 1 and not visited[i]:
#                 q.append(i)
#                 visited[i] = True
    
count = 0
for i in range(n):
    if not visited[i]:
        count += 1
        dfs(i)
        
print(count)