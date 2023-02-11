N,M=map(int,input().split())
A=[]
for i in range(M):
    c=int(input())
    a=list(map(int,input().split()))
    A.append(a)
Q=[False]*N
co=0
for i in range(2 ** M):
    for j in range(M):
        if (i>>j)&1==1:
            for a1 in A[j]:
                Q[a1-1]=True
    if Q.count(True)==N:
        co+=1
    Q=[False]*N
print(co)
