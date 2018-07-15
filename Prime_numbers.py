

#CHECK IF THE NUMBER IS PRIME OR NOT


n=int (input('write a number: '))
aux=2
prime=True

while (aux<n)and(prime):
    if n%aux !=0:
        aux=aux+1
    else:
        prime=False

if prime:
         print('the number written is prime')
else:
         print('the number written is not prime')

