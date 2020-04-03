def RevNum(num):
    sums = 0
    while num>0:
        d = num%10
        sums = 10*sums+d
        num = int(num/10)
    return sums

def ReverseString(st):
    s=st[::-1]
    return s
#print(RevNum(153))
#print(ReverseString("malayalam"))