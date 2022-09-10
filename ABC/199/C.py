N=int(input())
S=list(input())
Q=int(input())
co=0
for i in range(Q):
    t,a,b=map(int,input().split())
    if t==1:
        if co%2==1:
            S[(a+N-1)%(2*N)],S[(b+N-1)%(2*N)]=S[(b+N-1)%(2*N)],S[(a+N-1)%(2*N)]
        else: 
            S[a-1],S[b-1]=S[b-1],S[a-1]
            
    else:
        co+=1
if co%2==1:
    S=S[N:]+S[:N]
print(''.join(S))
