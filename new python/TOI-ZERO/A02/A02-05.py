W, H, M, N = map(int, input().split())
lisM = [0] + list(map(int, input().split())) + [W]
lisN = [0] + list(map(int, input().split())) + [H]

lengthM = []
i = 0
while i < len(lisM) - 1:
    lengthM.append(lisM[i+1] - lisM[i])
    i += 1
lengthN = []
j = 0
while j < len(lisN) - 1:
    lengthN.append(lisN[j+1] - lisN[j])
    j += 1

lengthM.sort(reverse=True)
lengthN.sort(reverse=True)

area1 = lengthM[0] * lengthN[0]
area2 = lengthM[1] * lengthN[0]
area3 = lengthM[0] * lengthN[1]

if area2 > area3:
    print(area1, area2)
else:
    print(area1, area3)
