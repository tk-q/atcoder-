N,W=map(int,input().split())
S=[]
T=[]
P=[]
from collections import defaultdict
d = defaultdict(int)
for i in range(N):
    s,t,p=map(int,input().split())
    d[s]+=p
    d[t]-=p
l=d.values()
l1=d.keys()
s=zip(l1,l)
s=sorted(s)
l1,l=zip(*s)
co=0
for m1 in l:
    co+=m1
    if co>W:
        print("No")
        exit()
print("Yes")
