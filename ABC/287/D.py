S=input()
T=input()
co=0
co1=0
m=""
P=[0]*(len(T)+1)
P1=[0]*(len(T)+1)
P[0]=1
P1[0]=1
for i in range(len(T)):
    if S[i]==T[i] or S[i]=="?" or T[i]=="?":
        co+=1
        P[i+1]=1
    else:
        break

for i in range(len(T)):
    if S[-(i+1)]==T[-(i+1)] or S[-(i+1)]=="?" or T[-(i+1)]=="?":
        co1+=1
        P1[i+1]=1
    else:
        break
for i in range(len(P)):
    if P[i]==1 and P1[len(P)-i-1]==1:
        print("Yes")
    else:
        print("No")
        
