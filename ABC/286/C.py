N,A,B=map(int,input().split())
S=input()
co=0
min1=10**20
for i in range(N):
    co+=i*A
    for k in range(N//2):
        if S[(k+i)%N]!=S[(N-1-k+i)%N]:
            co+=B
    min1=min(co,min1)
    co=0
print(min1)
