num = int(input())
lis = list(map(int, input().split()))
count = 0
for i in range(num):
    if i == 0:
        if lis[i] >= lis[i+1]:
            count += 1
    elif i == num-1:
        if lis[i] >= lis[i-1]:
            count += 1
    elif lis[i] >= lis[i-1] and lis[i] >= lis[i+1]:
        count += 1
print(count)