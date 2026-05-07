A = int(input())
B = []
for i in range(A):
    v = input().split()
    B.append(int(v[1]))
max_v = -1
no_sell = 0
for i in range(A-1, -1, -1):
    Value = B[i]
    if Value < max_v:
        no_sell += 1
    else:
        max_v = Value
print(no_sell)