# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import NumOps as no


def Palindrome(n):
    rev = no.RevNum(n)
    if rev == n:
        return True
    else:
        return False


def Armstrong(n):
    sumpowdig = no.SumPowDig(n)
    if sumpowdig==n:
        return True
    else:
        return False

def Perfect(n):
    sumfactor = no.SumFac(n)
    if sumfactor == n:
        return True
    else:
        return False

def PerfectSquare():
    pass


def main():
    pal=0
    arm=0
    per=0

    n = int(input("Enter your number: "))
    numcheck = input("Enter your choice (Palindrome/ Armstrong/ Perfect): ")
    
    if 'pal' in numcheck.lower():
        if Palindrome(n):
            pal+=1
    elif 'arm' in numcheck.lower():
        if Armstrong(n):
            arm+=1
    elif 'per' in numcheck.lower():
        if Perfect(n):
            per+=1
    else:
        print('Wrong Option!')
    
    if (pal==0) and (arm==0) and (per==0):
        print("The number is not "+ numcheck+'!')
    else:
        print("The number is "+ numcheck+'!')

if __name__ == "__main__":
    main()
