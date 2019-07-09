import numpy as np
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))
n = 10
a = [[0]*n for i in range(n)]
start=[9,9]
end=[2,5]
def new_a_star(a,start,end,dc,lc):
    h = [[0]*n for i in range(n)]
    f = [[0]*n for i in range(n)]
    ex,ey=end
    for i in range(n): #calculating heuristic values for all the nodes because the list is static
        for j in range(n):
            h[i][j] = (abs(ex-i)+abs(ey-j))*10
    sx,sy=start
    open,closed=[h[sx][sy]],[]
    #finding the elements of open List
    first = 0
    r=0
    while(len(open)>0 and r<15):
        r+=1
        if first==0:
            closed.append(open[0])
            open.remove(h[sx][sy])
            first=1
        x1 = sx-1
        if(x1<0): #to solve the problems happen at edges of the matrix
            x1=0
        x2= sx+2
        if(x2>n):#to solve the problems happen at edges of the matrix
            x2=n
        y1 = sy-1
        if(y1<0):#to solve the problems happen at edges of the matrix
            y1=0
        y2= sy+2
        if(y2>n):#to solve the problems happen at edges of the matrix
            y2=n
        g=[]
        q=0
        for i in range(x1,x2):
                for j in range(y1,y2):
                    if a[i][j]==-1 :
                        continue
                    if i==x2//2 and j==y2//2:
                        g.append(0)
                    elif (i+j)%2!=0:
                        g.append(lc)
                    else:
                        g.append(dc)
                    if (h[i][j] + g[q]) not in open:
                        open.append(h[i][j] + g[q])
                    f[i][j] = g[q]+h[i][j]
                    q+=1

        #finding the minimum element in open list
        minimum = min(open)
        closed.append(minimum)
        sx,sy = index_2d(f,minimum)
        if a[sx][sy]!=-1:
            a[sx][sy] = f[sx][sy]
        open.remove(minimum)
        print(open)
        # print(closed)
        # print(sx,sy)
        # print(g)
        # print(np.matrix(h))
        print(np.matrix(a))
    #return closed,f
new_a_star(a,start,end,14,10)
