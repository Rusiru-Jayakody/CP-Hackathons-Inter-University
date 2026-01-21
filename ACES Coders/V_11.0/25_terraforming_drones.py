import sys
input = sys.stdin.readline
r,c,n = map(int, input().split())
grid = []
for i in range(r):
    s = input().strip()
    row = []
    for j in range(c):
        row.append(s[j])
    grid.append(row)
    
def burst(r, c, current_grid):
    new_grid = [['D'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if current_grid[i][j] == 'D':
                new_grid[i][j] = '.'
                if i > 0: new_grid[i-1][j] = '.'
                if i < r-1: new_grid[i+1][j] = '.'
                if j > 0: new_grid[i][j-1] = '.'
                if j < c-1: new_grid[i][j+1] = '.'
    return ["".join(row) for row in new_grid]

if n <= 1:
    for i in range(r):
        print("".join(grid[i]))
elif n % 2 == 0:
    row = ['D']*c
    for _ in range(r):
        print("".join(row))
else:
    state_3 = burst(r, c, grid)
    if n % 4 == 3:
        print("\n".join(state_3))
    else: 
        state_5 = burst(r, c, state_3)
        print("\n".join(state_5))


                    
    