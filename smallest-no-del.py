from itertools import combinations
r,m=map(int,input().split())
a=len(str(r))
l=list(combinations(str(r),a-m))
l=sorted(l)
print(*l[0],sep= '')
