n=int(input())
x,y=map(int,input().split())
if(n in range(x+1,y-1)):
  print("yes")
else:
  print("no")
