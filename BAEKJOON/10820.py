import sys
import string

read=sys.stdin.readline

while(True):
    low=high=num=space=0

    line=read()[:-1]
    if line=='':
        break

    for a in line:
        if a in string.ascii_lowercase:
            low+=1
        elif a in string.ascii_uppercase:
            high+=1
        elif a==' ':
            space+=1
        else:
            num+=1
    print('{} {} {} {}'.format(low,high,num,space))
        