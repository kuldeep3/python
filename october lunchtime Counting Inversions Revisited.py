t=int(input())
while(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1=[]
    l2=[]
    for i in l:
        key=0
        c=0
        while(key<n):
            if(l[key]<i):
                c+=1
            key+=1
        l1.append(c)
    sum_new=0
    for i in l1:
        sum_new+=i
    isum=0
    isum+=sum_new*(k*(k-1))//2
    x=0
    while(x<n):
        c=0
        key=x
        while(key<n):
            if(l[key]<l[x]):
                c+=1
            key+=1
        l2.append(c)
        x+=1
    sum_latest=0
    for i in l2:
        sum_latest+=i
    isum+=sum_latest*k
    #print(l2)
    print(isum)
    t-=1
