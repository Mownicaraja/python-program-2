def rw(s):
    return ' '.join(x[::-1] for x in s.split(" "))
s=str(input())
print(rw(s))
