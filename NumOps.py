def RevNum(num):
    rev = 0
    while num != 0:
        d = num % 10
        #sum += d
        #sum2 += pow(d,p)
        rev = 10*rev + d
        num = int(num/10)

    return rev

def SumDig(num):
    sum = 0
    while num != 0:
        d = num % 10
        sum += d
        num = int(num/10)
    return sum

def NoDig(num):
    p=0
    while num!=0:
       p=p+1
       num = int(num/10)
    return p

def SumPowDig(num):
    sumpow = 0
    p = NoDig(num)
    while num != 0:
        d = num % 10
        sumpow += pow(d,p)
        num = int(num/10)
    return sumpow

def SumFac(num):
    i=1
    sumfactor = 0
    while i<num:
        if(num%i==0):
            sumfactor += i
        i=i+1
    return sumfactor

def Factorial(num):
    i = 1
    fact = 1
    for i in range(num):
        fact *= (i+1)
    return fact

if __name__ == "__main__":
    print(Factorial(5))
    