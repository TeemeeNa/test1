n = int(input())
grid = [input() for _ in range(n)]

reach = [[False] * n for _ in range(n)]

for r in range(n - 1, -1, -1):
    for c in range(n - 1, -1, -1):
        if grid[r][c] == 'X':
            continue
            
        if r == n - 1 and c == n - 1:
            reach[r][c] = True
        else:
            down = reach[r+1][c] if r + 1 < n else False
            right = reach[r][c+1] if c + 1 < n else False
            
            if down or right:
                reach[r][c] = True

ans = 0
for row in reach:
    for item in row:
        if item:
            ans += 1

print(ans)