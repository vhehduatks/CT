import sys
read=sys.stdin.readline

A,B,C=map(int,read().split())

print((A+B)%C)
print(((A%C)+(B%C))%C)

print((A*B)%C)
print(((A%C)*(B%C))%C)