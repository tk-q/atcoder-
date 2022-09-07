#https://atcoder.jp/contests/abc266/tasks/abc266_c
Ax,Ay=map(int,input().split())
Bx,By=map(int,input().split())
Cx,Cy=map(int,input().split())
Dx,Dy=map(int,input().split())
import math
a=(math.atan2(Ay - By, Ax - Bx) - math.atan2(Cy - By, Cx - Bx)) / math.pi * 180
b=(math.atan2(By - Cy, Bx - Cx) - math.atan2(Dy - Cy, Dx - Cx)) / math.pi * 180
c=(math.atan2(Cy - Dy, Cx - Dx) - math.atan2(Ay - Dy, Ax - Dx)) / math.pi * 180
d=(math.atan2(Dy - Ay, Dx - Ax) - math.atan2(By - Ay, Bx - Ax)) / math.pi * 180
if a<0:
    a=360+a
if b<0:
    b=360+b
if c<0:
    c=360+c
if d<0:
    d=360+d
if a<180 and b<180 and c<180 and d<180:
    print("Yes")
else:
    print("No")
