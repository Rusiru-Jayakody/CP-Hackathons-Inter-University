import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s,h = map(int, input().split())
    colors = {}
    for i in range(h):
        l,r = map(int,input().split())
        colors[i+1] = (l,r)
    hats = list(map(int, input().split()))    
    count = 0
    
    for i in range(s):
        x = 0
        seen = set()
        less = set()
        arr = [0] * (h+1)
        arr[hats[i]] += 1
        if colors[hats[i]][0] <= arr[hats[i]] <= colors[hats[i]][1]:
            x += 1
            seen.add(hats[i])
        elif arr[hats[i]] < colors[hats[i]][0]:
            less.add(hats[i])
        
        for j in range(i+1,i+s-1):
            temp = j
            if j >= s:
                temp = j - s
            arr[hats[temp]] += 1
            if colors[hats[temp]][0] <= arr[hats[temp]] <= colors[hats[temp]][1]:
                if hats[temp] not in seen:
                    x += 1
                    seen.add(hats[temp])
                if hats[temp] in less:
                    less.remove(hats[temp])
                if x == h or len(less)== 0:
                    count += 1
            elif arr[hats[temp]] > colors[hats[temp]][1]:
                break
            elif arr[hats[temp]] < colors[hats[temp]][0]:
                less.add(hats[temp])                           
    print(count)
            
            
    
    