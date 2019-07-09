def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

n = 10
a = [[0]*n for i in range(n)]
def a_star(a,start,end,dc,lc): # array, start, end, diagonal cost, linear cost
    temp=[]
    x,y=start
    k,l=end
    m,n=start
    g=0
    closed=[a[x][y]]
    while([x,y]!=end):
        open=[]
        heu=[]

        for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    b=[i,j]
                    if((a[i][j]==-1)):
                        continue
                    if(b in closed):
                        continue
                    h=(k-i+l-j)*10
                    if((i+j)%2!=0):
                        p = lc
                    else:
                        p = dc
                    a[i][j]=g + h + p
                    open.extend([a[i][j]])
        print(open)
        x,y=index_2d(a,min(open))]
        if(x+y%2!=0):
            g+=lc
        else:
            g+=dc
        closed.append([x,y])
        print(x,y)
    return closed
temp = a_star(a,[1,1],[8,8],14,10)
print(temp)
