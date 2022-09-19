N=int(input())
P=10**4
min1=P
tmp=0
A,B,C=map(int,input().split())
for x in range(P):
    for y in range(P):
        tmp=A*x+B*y
        if (N-tmp)%C!=0 or tmp>N:
            continue
        z=x+y+(N-tmp)//C
        if min1>z:
            min1=z
print(min1)
