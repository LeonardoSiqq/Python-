frase = input('Escreva uma frase: ')
count = 0
for letra in frase:
 if letra in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
  count += 1
  print(F'A frase possui {count} consoantes.')

  
 