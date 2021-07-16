import sys
read=sys.stdin.readline

A,B=map(int,read().split())
m=int(read())-1
A_num=list(map(int,read().split()))

def A_to_dec(A,A_num,m):
    ret=0
    while m>=0:
        temp=A**m
        temp_A=A_num.pop(0)
        ret+=temp*temp_A
        m-=1
    return ret

def dec_to_B(Dec,B):
    ret=''
    if Dec>=B:
        quotient=Dec//B
        remain=Dec%B
        ret=str(remain)
    else:
        return str(Dec)
    return dec_to_B(quotient,B)+' '+ret

print(dec_to_B(A_to_dec(A,A_num,m),B))