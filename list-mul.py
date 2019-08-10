def ml(li) : 
    rslt = 1
    for x in li: 
         rslt = rslt * x  
    return abs(rslt)  
n=int(input())
a=list(map(int,input().split()))[:n] 
print(ml(a))
