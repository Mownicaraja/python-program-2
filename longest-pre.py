def minl(a,n):
    min=len(a[0])
    for i in range(1,n):
        if len(a[i])<min:
           min=len(a[i])
    return(min)
def commonprefix(a,n):
    minlen=minl(a,n)
    result=""
    for i in range(minlen):
        crn=a[0][i]
        for j in range(1,n):
            if(a[j][i]!=crn):
                return result
        result=result+crn
    return(result)
if __name__=="__main__":
    no=int(input())
    a=[]
    for x in range(0,no):
        ss=str(input())
        a.append(ss)
    n=len(a)
    final=commonprefix(a,n)
    if(len(final)):
        print(final)
    else:
        print("")
