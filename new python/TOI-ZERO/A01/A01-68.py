A = int(input())
B = input()
C = list(map(int, B.split()))
D = 0
result = ""

for i in range(A):
    D += C[i]
point = f"{D / A:.1f}"  
if float(point) >= 60:
    result = "PASS"
else:
    result = "FAIL"

for i in range(A):
    if C[i] < 50:
        result = "FAIL"
        break

print(f"{point}")
print(result)