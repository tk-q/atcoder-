N,X,Y=map(int,input().split())
S=1
S1=0
NS=0
NS1=0
max1=0
while (N>1):
    if S!=0:
        NS+=S
        S1+=X*S
    if S1!=0:
        NS+=S1
        NS1+=Y*S1
    S1=NS1
    S=NS
    max1=max(max1,S1)
    NS1=0
    NS=0
    N-=1
print(S1)


