from random import randint
T = int(input())
for i in range(0,T):
    A,B = input().split()
    A=int(A)
    B=int(B)
    N = int(input())
    for i in range(0,N):
        Q=randint(A+1,B)
        print(Q)
        word = input()
        if word=='CORRECT':
            break
        elif word=='TOO_SMALL':
            A=Q
        elif word == 'TOO_BIG':
            B=Q-1
        else:
            break