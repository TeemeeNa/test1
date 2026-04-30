import math
A = input()
B = int(input())
C = 0
for i in range(B):
    D = float(input())
    C += D
if A == "Y":
    C = (C*95)/100
elif A == "N" and C >= 500:
    C = (C*97)/100
else:
    C = C
rounded_C = math.ceil(C * 100) / 100
print(f"{rounded_C:.2f}")