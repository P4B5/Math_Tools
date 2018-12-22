

#PHYTON CALCULATOR

import math

print ('--------------------THIS IS A CALCULATOR----------------------')

print ('')

print('First, write the two numbers to work with:')

print ('')

number1 = float (input ('Number 1:'))                      
number2 = float (input ('Number 2:'))

print ('')

print ('Second, choose the operation you want to do:')
print (sep='')
print ('ADDITION  --------------------------> write 1')
print ('SUBSTRACTION  ----------------------> write 2')
print ('MULTIPLICATION ---------------------> write 3')
print ('DIVISION  --------------------------> write 4')
print ('REMAINDER --------------------------> write 5')
print ('POWER ------------------------------> write 6')
print ('SQUARE ROOT (**only number 1**) ----> write 7')

print ('')

A=int (input('operation to do:'))

print ('')

if A<0 or A>7:
    print('this number doesnt correspond with any operation')

elif A==1:
    addition = number1+number2
    print('THE RESULT IS: ', addition)
elif A==2:
    substraction = number1-number2
    print('THE RESULT IS: ', substraction)
elif A==3:
    multiplication = number1*number2
    print('THE RESULT IS: ', multiplication)                      
elif A==4:
    division= number1/number2
    print('THE RESULT IS: ', division)
elif A==5:
    remainder=number1%number2
    print('THE RESULT IS: ', remainder)
elif A==6:
    power= number1**number2
    print('THE RESULT IS: ', power)
elif A==7:
    root=math.sqrt(number1)
    print('THE RESULT IS: ',root )

