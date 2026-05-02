nums = int(input())
lis = []
for i in range(nums):
    A = int(input())
    lis.append(A)
lis.sort()

last = -1
stacks = 0
Count = 0

for size in lis:
    if size == last:
        Count += 1
    else:
        Count = 1
        last = size
    
    if Count > stacks:
        stacks = Count

print(stacks)