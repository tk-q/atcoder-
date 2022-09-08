N=int(input())
A=list(map(int,input().split()))
from collections import Counter
co1=0
L=[]
left=0
right=0
for i in range(len(A)):
    if i+1==A[i]:
        co1+=1
    left=i+1
    right=A[i]
    if i+1>A[i]:
        left=A[i]
        right=i+1
    L.append((left,right))

counter = Counter(L)
co2=0

for m in (counter.values()):
    if m==2:
        co2+=1
if co1>=2:
    co1=(co1*(co1-1))//2
else:
    co1=0
print(co1+co2)


