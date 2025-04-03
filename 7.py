n = int(input('escreva um número inteiro: '))
mult = 0

for i in range(2, n):
   if n % i == 0 :
      mult += 1
     
if mult > 0:
      print('o número não é primo')

else:

      print('o número é primo')
      