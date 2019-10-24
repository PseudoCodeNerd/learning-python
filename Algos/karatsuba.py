def karatsuba(x, y):
    sX = str(x)
    sY = str(y)
    if (x < 10) and (y < 10):
        return (x*y)
    m = max(len(sX), len(sY))
    m2 = m // 2 
    
    a = x // 10**(m2)
    b = x % 10**(m2)
    c = y // 10**(m2)
    d = y % 10**(m2)
    
    z0 = karatsuba(b,d)
    z1 = karatsuba((a+b), (c+d))
    z2 = karatsuba(a, c)
    
    return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + z0
x= 2718281828459045235360287471352662497757247093699959574966967627
y = 3141592653589793238462643383279502884197169399375105820974944592
print(karatsuba(x, y))