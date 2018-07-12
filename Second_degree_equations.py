

import math
from math import pi

a= int (input('write the coeficient a: '))
b= int (input('write the coeficient b: '))
c= int (input('write the coeficient c: '))

print ('the solution of the ecuation', a, 'x^2', '+', b, 'x', '+', c, '=0 es:')

if a==0:
    if b==0:
        if c==0:
            print ('any number is solution')
        else:
            print ('it hasnt got solution')
    else:
        print ('an only real root: ', -c/b)
else:
    disc=(b**2)-(4**a*c)
    if disc>0:
        x1=(-b+sqrt(disc)/(2*c))
        x2=(-b-sqrt(disc)/(2*a))
        print('two real roots: ', x1, 'y', x2)

    else:
        preal=-b/(2*a)
        pimag=(math.sqrt(-disc)/(2*a))
        print ('two complex roots: ', preal, '(+/-)', pimag, 'i')

