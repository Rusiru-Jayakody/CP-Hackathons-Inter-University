n = int(input())
count = 0
digits = [0,1,6,8,9]
rotated = {0:0,1:1,6:9,8:8,9:6}
count = [0]

def is_confusing(x):
    original = x
    rotate = 0
    while x > 0:
        rotate = (rotate*10) + rotated[x%10]
        x //= 10
    return rotate != original
    
def dfs(num):
    if num > n:
        return
    if is_confusing(num):
        count[0] += 1
    for d in digits:
        if d == 0 and num == 0:
            continue
        dfs(num*10 + d)

dfs(0)
print(count[0])