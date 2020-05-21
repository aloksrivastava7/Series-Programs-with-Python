'''

SERIES (Hacker Rank) :

(a + 2^0.b),(a + 2^0.b + 2^1.b),(a + 2^0.b + 2^1.b + ....),.......,n

'''
#PROGRAM

T = int(input())
while T!=0:
    a,b,n = (input()).split(' ')
    for i in range(0,int(n)):
        res = 0
        for j in range(0,i+1):
            res = res + (int(pow(2,j))*int(b))
        s = int(a) + res
        print(s,end = ' ')
    print()
    T = T - 1
