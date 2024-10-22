###Questão 01: Escreva um algoritmo em Python que leia uma lista de 10 elementos inteiros. Ao final mostre qual foi o menor elemento recebido e sua posição original (tempo de inserção) dentro da lista.


lista =[]
me = 0
for p in range(0,10):
    lista.append(int(input(f"Ponha um valor na lista da posição {p}: ")))
    if p == 0:
        me = lista[p]
    elif lista[p] < me:
        me = lista[p]

print('<>'*30)
print(f'Os valores da lista foram:{lista}')
print(f'Sendo o menor valor:{me}\n que ficou na posição:', end='')
for i , v in enumerate(lista):       
   if v == me:
      print(f'{i}')