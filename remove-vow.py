def rv(s):
    vow=('a','e','i','o','u','A','E','I','O','U')
    for x in s:
        if x in vow:
            s=s.replace(x,"")
    a=s[::-1]
    print(a)
s=str(input())
rv(s)
