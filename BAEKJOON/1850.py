# import sys
# read=sys.stdin.readline

# a,b=map(int,read().split())
# if a>b:
#     a,b=b,a

# def gcd(a,b):
#     while(b>0):
#         r=a%b
#         a=b
#         b=r
#     return a
# print(gcd(30,31))
# # print('1'*gcd(3,6))


def gcd(a,b):
    if a>b:
        a,b=b,a
    while(b>0):
        r=b%a
        b,a=a,r

    return b
print(gcd(31,30))