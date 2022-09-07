import numpy as np
Ax,Ay=map(int,input().split())
Bx,By=map(int,input().split())
Cx,Cy=map(int,input().split())
Dx,Dy=map(int,input().split())
 
b = np.array([Ax-Bx,Ay-By])
a = np.array([Cx-Bx,Cy-By])
 
   #配列aとbの内積
b1 = np.array([Bx-Cx,By-Cy])
a1 = np.array([Dx-Cx,Dy-Cy])
 
b2 = np.array([Cx-Dx,Cy-Dy])
a2 = np.array([Ax-Dx,Ay-Dy])
 
b3 = np.array([Dx-Ax,Dy-Ay])
a3= np.array([Bx-Ax,By-Ay])
 
if np.cross(a,b)>=0 and np.cross(a1,b1)>=0 and np.cross(a2,b2)>=0 and np.cross(a3,b3)>=0:
    print("Yes")
else:
    print("No")
