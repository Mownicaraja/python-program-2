def factors(n):
    for i in range(1,n+2):
        if n%i==0:
            ans=i
            if(ans%2)==0:
                print(ans,end=" ")
num=int(input())
factors(num)
