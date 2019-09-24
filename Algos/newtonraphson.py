'''
Newton-Raphson Method (Used this yesterday in my logistic regression code; found it out to be cool...)
@author: Me 
'''
from sympy import diff
from decimal import Decimal

def NewtonRaphson(func, a):
    ''' Finds root from the point 'a' onwards'''
    while True:
        c = Decimal(a) - ( Decimal(eval(func)) / Decimal(eval(str(diff(func)))) )
        a = c
        # 'c' indicates accuracy
        if  abs(eval(func)) < 10**-15:
            return  c

#   Examples
if __name__ == '__main__':
    # Finding Pi
    print('sin(x) = 0', NewtonRaphson('sin(x)', 2))

    # Finding Square Root of 569
    print('x**2 - 69 = 0', NewtonRaphson('x**2 - 69', 0.1))

    # Finding Exponential Roots
    print('exp(x) - 1 = 0', NewtonRaphson('exp(x) - 1', 0))
