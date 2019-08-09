num=int(input())
to=0
while(num>0):
    dig=num%10
    to=to+dig
    num=num//10
print(to)
