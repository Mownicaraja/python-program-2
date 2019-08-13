from statistics import median
n=int(input())
li=list(map(int,input().split()))[:n]
print(median(li))
