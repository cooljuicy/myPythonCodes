from math import pi,sqrt
from time import process_time
from juicy import fd
def factorial(n):
    a=1
    for i in range(2,n+1):
        a*=i
    return a
def sery(n):
    a=factorial(4*n)
    b=factorial(n)**4
    c=1103+26390*n
    d=(4*99)**(4*n)
    return a/b*c/d
def findan(n):
    a=0
    for i in range(n+1):
        a+=sery(i)
    a=a*2*sqrt(2)/9801
    return a
print(1/findan(10))
print(process_time())