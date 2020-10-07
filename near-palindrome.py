n=int(input())
s=str(n)
l=len(s)
if l%2==0:
    if s=='9'*len(s):
        print(n+2)
    else:
        mid=l//2
        c=l-mid-1
        if s[mid]!='9':
            c=11*(10**c)
            print(n+c)
        else:
            while s[mid]=='9':
                mid+=1 
            c=l-mid-1
            c=11*(10**c)
            print(n+c)
else:
    if s=='9'*len(s):
        print(n+2)
    else:  
        mid=l//2
        c=l-mid-1
        if s[mid]!='9':
            c=10**c
            print(n+c)
        else:
            while s[mid]=='9':
                mid+=1 
            c=l-mid-1
            c=11*(10**c)
            print(n+c)
        