m=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(m):
    j=0
    row=0
    col=0
    while j<len(m[i]):
        row=row+m[i][j]
        col=col+m[j][i]
        j=j+1
    i=i+1
    a=0
    b=0
    c=len(m)-1
    d1=0
    d2=0
    while a<len(m):
        d1=d1+m([a][b])
        d2=d2+m([b][c])
        a=a+1
        b=b+1
        c=c+1
if row==col==d1==d2:
    print("Magic no")
else:
    print("nhi hai")