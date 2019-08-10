num=int(input())
i=1
while(i<=num):
    count=0
    if(num%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                count=count+1
            j=j+1
        if(count==2):
            print(i,end=" ")
    i=i+1
