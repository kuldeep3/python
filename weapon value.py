def xoring(a,b):
    s=""
    j=0
    while(j<10):
        s+=str(int(a[j])^int(b[j]))
        j+=1
    return s
#print(xoring("0000000000","1010101011"))
t=int(input())
while(t):
    x=[]
    n=int(input())
    m=n
    while(m):
        x.append(input())
        m-=1
    k="0000000000"
    l=0
    #print(x)
    while(l<n):
        k=xoring(k,(x[l]))
        #print(k)
        l+=1
    print(k.count("1"))
    t-=1
