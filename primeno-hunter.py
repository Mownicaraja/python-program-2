r=int(input())
for i in range(2,r+1):
    m=0
    for s in range (2,i//2+1):
        if(i%s==0):
            m=m+1
    if(m<=0):
        print(i,end=" ")
