N = int(input())
grid = []
count = 1
for i in range(N):
    row = input()
    grid.append(row)

for j in range(N):
    for k in range(N):
        if grid[j][k] == '.':
            count += 1