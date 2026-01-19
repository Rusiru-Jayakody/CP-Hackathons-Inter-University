from collections import deque
n = int(input())
i = 1
stk = [1]
while i < n:
    q = deque(stk)
    stk = []
    while q:
        l = q[0]
        count = 0
        while q and q[0] == l:
            q.popleft()
            count += 1
        stk.append(count)
        stk.append(l)
    i += 1
    
print("".join(map(str,stk)))
