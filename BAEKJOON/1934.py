import sys 
read=sys.stdin.readline

t=int(read())
for _ in range(t):
    a,b=map(int,read().split())
    c=range(1,max(a,b)+1)
    temp=[]

    for i in c:
        if a%i==0 and b%i==0:
            temp.append(i)

    print(a*b//temp[-1])