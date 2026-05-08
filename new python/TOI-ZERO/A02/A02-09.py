Team_Cred = list(map(int, input().split()))
Team_num_total = Team_Cred[0]
Cred = Team_Cred[1]

All_T = []
for _ in range(Team_num_total):
    row = list(map(int, input().split()))
    All_T.append(row)

Team_num = list(range(1, Team_num_total + 1))
Card = True if Cred > 0 else False

while len(Team_num) > 1:
    winner = []
    for i in range(0, len(Team_num), 2):
        A = Team_num[i]
        B = Team_num[i+1]       
        WINNER = All_T[A-1][B-1]
        
        if Card:
            if A == Cred and WINNER != Cred:
                WINNER = Cred
                Card = False
            elif B == Cred and WINNER != Cred:
                WINNER = Cred
                Card = False 
        winner.append(WINNER)
    Team_num = winner
print(Team_num[0])