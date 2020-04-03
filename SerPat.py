"""Stores all common/uncommon series/pattern."""
import NumOps as no

class patternStar:
    def __init__(self,n=5):
        self.n = n

    def patternStar1(self):
        for i in range(1,self.n+1):
            for j in range(1,self.n+1):
                print('*',end='')
            print()

    def patternStar2(self):
        for i in range(1,self.n+1):
            for j in range(1,i+1):
                print('*',end='')
            print()

    def patternStar3(self):
        i=self.n
        while i>0:
            for j in range(1,i+1):
                print('*',end="")
            print()
            i-=1

class patternNum:
    def __init__(self,n=5):
        self.n=n
    
    def patternNum1(self):
        for i in range(self.n):
            for j in range(self.n):
                print(i+1,end=' ')
            print()

    def patternNum2(self):
        for i in range(self.n):
            for j in range(self.n):
                print(j+1,end=' ')
            print()

    def patternNum3(self):
        for i in range(1,self.n+1):
            for j in range(1,i+1):
                print(i,end=' ')
            print()

    def patternNum4(self):
        for i in range(1,self.n+1):
            for j in range(1,i+1):
                print(j,end=' ')
            print()

    def patternNum5(self):
        i=self.n
        while i>0:
            for j in range(self.n):
                print(i,end=' ')
            print()
            i-=1

    def patternNum6(self):
        i=self.n
        while i>0:
            for j in range(i):
                print(i,end=' ')
            print()
            i-=1

    def patternNum7(self):
        i=self.n
        while i>0:
            for j in range(self.n):
                print(j+1,end=' ')
            print()
            i-=1

    def patternNum8(self):
        i=self.n
        while i>0:
            for j in range(i):
                print(j+1,end=' ')
            print()
            i-=1

class series:
    def __init__(self,n=50):
        self.n=n    

    def Fibonacci(self):
        a=0
        b=1
        fb = [0,1]
        for i in range(self.n):
            c=a+b
            fb.append(c)
            a=b
            b=c
        return fb

    def Fourier(self):
        pass

    def Arithmetic(self):
        a = float(input('First term: '))
        d = float(input('Difference: '))
        As = []
        for i in range(self.n):
            As.append(a)
            a+=d  
        return As 

    def Geometric(self):
        while True:
            a = float(input('Enter first term: '))
            if a==0:
                print('First term can\'t be zero')
            else:
                break
        r = float(input('Common ratio: '))
        Gs = []
        for i in range(self.n):
            Gs.append(a)
            a *= r
        return Gs

    def Logarithmic(self):
        Ls = []
        while True:
            a_n = float(input("Enter x: "))
            if a_n<=-1 or a_n>1:
                print('A valid logarithmic series can\'t be achieved with this value of x. x has to be in the range (-1,1].')
            else:
                for i in range(1,self.n+1):
                    t_n = pow(-1,i+1)*pow(a_n,i)/i
                    Ls.append(t_n)
                return Ls

    def Exponential(self):
        a_n = float(input('Enter x: '))
        Es = []
        for i in range(self.n):
            t_n = pow(a_n,(i))/no.Factorial(i)
            Es.append(t_n)
        return Es


if __name__ == "__main__":
    #n = int(input('Enter the number of terms/rows: '))
    
    #ps = patternStar()
    #pn = patternNum()
    se = series(10)

    #Fibonacci()

    #ps.patternStar1()
    #ps.patternStar2()
    #ps.patternStar3()
    
    #pn.patternNum1()
    #pn.patternNum2()
    #pn.patternNum3()
    #pn.patternNum4()
    #pn.patternNum5()
    #pn.patternNum6()
    #pn.patternNum7()
    #pn.patternNum8()
    
    #print(se.Fibonacci())
    #print(se.Arithmetic())
    #print(se.Geometric())
    #print(se.Logarithmic())
    #print(se.Exponential())
    
    